import data_viz
import gzip

# Linear Search Function with input validation
def linear_search(key, L):
    if L is None:
        return None
    if len(L) == 0:
        return -1
    if not isinstance(L, list):
        raise TypeError('Input must be list')
    for i in range(len(L)):
        curr = L[i]
        if not type(key) == type(curr):
            raise TypeError('key and list elements must be same types')
        if key == curr:
            return i
    return -1

# Binary search function in input validation
def binary_serach(key, L):
    pass


def main():
    # Defines file names
    data_file_name = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
    sample_info_file_name = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'

    # Defines variable names
    sample_id_col_name = 'SAMPID'
    tissue_group_col_name = 'SMTS'
    tissue_type_col_name = 'SMTSD'
    gene_name = 'BRCA2'

    # samples is a list that stores each sample and it's attributes as a list within the larger list
    # info_header is a parrel array to each list element within samples
    samples = []
    info_header = None

    try:
        for l in open(sample_info_file_name):
            if info_header == None:
                info_header = l.rstrip().split('\t')
            else:
                samples.append(l.rstrip().split('\t'))
    except ValueError:
        print('Could not read sample info file')

    # stores the index of attributes for samples/info_header arrays
    tissue_group_col_idx = linear_search(tissue_group_col_name, info_header)
    tissue_type_col_idx = linear_search(tissue_type_col_name, info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, info_header)

    # group is an array that stores each tissue group
    # groupmembers stores lists of sample IDs of groups in the same index location as the group array
    # same applies for types, typemembers
    groups = []
    groupmembers = []
    types = []
    typemembers = []

    for row_idx in range(len(samples)):
        sample = samples[row_idx]
        sample_name = sample[sample_id_col_idx]
        curr_group = sample[tissue_group_col_idx]
        curr_type = sample[tissue_type_col_idx]
        curr_group_idx = linear_search(curr_group, groups)
        curr_type_idx = linear_search(curr_type, types)

        if curr_group_idx == -1:
            curr_group_idx = len(groups)
            groups.append(curr_group)
            groupmembers.append([])

        groupmembers[curr_group_idx].append(sample_name)

        if curr_type_idx == -1:
            curr_type_idx = len(types)
            types.append(curr_type)
            typemembers.append([])

        typemembers[curr_type_idx].append(sample_name)

    # group_counts stores the associated gene counts for each sample within lists
    # at the same index position as their groups
    group_counts = [ [] for i in range(len(groups)) ]
    type_counts = [ [] for i in range(len(types)) ]

    version = None
    dim = None
    data_header = None

    gene_name_col = 1

    for l in gzip.open(data_file_name, 'rt'):
        if version == None:
            version = l
            continue

        if dim == None:
            dim = [int(x) for x in l.rstrip().split()]
            continue

        if data_header == None:
            data_header = l.rstrip().split('\t')
            continue

        A = l.rstrip().split('\t')

        if A[gene_name_col] == gene_name:
            for group_idx in range(len(groups)):
                for member in groupmembers[group_idx]:
                    member_idx = linear_search(member, data_header)
                    if member_idx != -1:
                        group_counts[group_idx].append(int(A[member_idx]))

            for type_idx in range(len(types)):
                for member in typemembers[type_idx]:
                    member_idx = linear_search(member, data_header)
                    if member_idx != -1:
                        type_counts[type_idx].append(int(A[member_idx]))
            break

    data_viz.boxplot(group_counts, groups, 'Gene Expression of Tissue Group', 'Tissue Group = SMTS',
                     'Counts','tissue_group.png')
    data_viz.boxplot(type_counts, types, 'Gene Expression of Tissue Type', 'Tissue Type = SMTSD',
                     'Counts', 'tissue_type.png')

if __name__ == '__main__':
    main()
