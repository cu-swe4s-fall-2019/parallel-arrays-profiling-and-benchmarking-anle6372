"""Data visualization for RNA reads

Parameters
----------
gene_reads : gzipped .gct file containing the gene reads
sample_attributes: .txt library containing attributes for samples
gene : gene name to be analyzed
group_type : group to analyze genes within
output_file : name of resulting boxplot figure

Returns
-------
output_file : boxplot figure that shows expression of gene across group_type
"""

import data_viz
import gzip
import argparse
import sys
sys.path.insert(1, "/Users/Acer/Documents"
                   "/Python/parallel-arrays-profiling-"
                   "and-benchmarking-anle6372/"
                   "hash-tables-anle6372"
                   "")
import hash_tables as ht
import hash_functions as hf


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
def binary_search(key, L):
    lo = -1
    hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def main():
    # Argparse Defns
    parser = argparse.ArgumentParser(description='Plot gene expression for'
                                                 ' tissue type and '
                                                 'tissue group given a gene')

    parser.add_argument('--gene_reads', type=str,
                        help='File containing gene reads', required=True)

    parser.add_argument(
        '--sample_attributes', type=str,
        help='File containing the sample attributes', required=True)

    parser.add_argument(
        '--gene', type=str,
        help='Name of the gene you wish to analyze', required=True)

    parser.add_argument(
        '--group_type', type=str,
        help='Name of the group of samples you wish to analyze expression for',
        required=True)

    parser.add_argument(
        '--output_file', type=str,
        help='Name of the file the boxplot will be saved to', required=True)

    args = parser.parse_args()

    # Defines file names
    data_file_name = args.gene_reads
    sample_info_file_name = args.sample_attributes

    # Defines variable names
    sample_id_col_name = 'SAMPID'
    tissue_group_col_name = args.group_type
    gene_name = args.gene

    # samples is a list that stores each
    # sample and it's attributes as a list within the larger list
    # info_header is a parallel array to each list element within samples
    samples = []
    info_header = None
    try:
        num_samp = 0
        for l in open(sample_info_file_name):
            if info_header is None:
                info_header = l.rstrip().split('\t')
            else:
                samples.append(l.rstrip().split('\t'))
                num_samp += 1
    except ValueError:
        print('Could not read sample info file')
    N_samp = int(100000)
    N_groups = 1000

    # Initalizes hash tables
    group_table = ht.ChainedHash(N_groups, hf.h_rolling)
    read_table = ht.LinearProbe(N_samp, hf.h_rolling)

    # stores the index of attributes for samples/info_header arrays
    tissue_group_col_idx = linear_search(tissue_group_col_name, info_header)
    sample_id_col_idx = linear_search(sample_id_col_name, info_header)

    # writes the first hash table
    try:
        for row_idx in range(len(samples)):
            sample = samples[row_idx]
            sample_name = sample[sample_id_col_idx]
            curr_group = sample[tissue_group_col_idx]
            group_table.add(curr_group, sample_name)
    except ValueError:
        print('Could not assign Sample IDs')

    version = None
    dim = None
    data_header = None
    gene_name_col = 1

    try:
        for l in gzip.open(data_file_name, 'rt'):
            if version is None:
                version = l
                continue

            if dim is None:
                dim = [int(x) for x in l.rstrip().split()]
                continue

            # Sorts the data header so binary_search can be utilized
            if data_header is None:
                data_header = []
                i = 0
                for field in l.rstrip().split('\t'):
                    data_header.append([field, i])
                    i += 1
                data_header.sort(key=lambda tup: tup[0])

            A = l.rstrip().split('\t')
            if A[gene_name_col] == gene_name:
                for i in range(2, len(data_header)-2):
                    read_table.add(str(data_header[i][0]), A[i])
    except ValueError:
        print('Could not read data info file')

    # group_counts stores the associated
    # gene counts for each sample within lists
    # at the same index position as their groups
    groups = list(set(group_table.keys))
    group_counts = [[] for i in range(len(groups))]
    for group in range(len(groups)):
        for i in range(len(group_table.T)):
            if group_table.T[i] != []:
                if group_table.T[i][0][0] == groups[group]:
                    for sample in range(len(group_table.T[i])):
                        read = read_table.search(str(
                            group_table.T[i][sample][1]))
                        if read is not None:
                            group_counts[group].append(int(read))

    # This portion utilized parallel arrays
    # # samples is a list that stores each
    # # sample and it's attributes as a list within the larger list
    # # info_header is a parallel array to each list element within samples
    # samples = []
    # info_header = None
    #
    # try:
    #     for l in open(sample_info_file_name):
    #         if info_header is None:
    #             info_header = l.rstrip().split('\t')
    #         else:
    #             samples.append(l.rstrip().split('\t'))
    # except ValueError:
    #     print('Could not read sample info file')
    #
    # # stores the index of attributes for samples/info_header arrays
    # tissue_group_col_idx = linear_search(tissue_group_col_name, info_header)
    # sample_id_col_idx = linear_search(sample_id_col_name, info_header)
    #
    # # group is an array that stores each tissue group
    # # groupmembers stores lists of sample IDs of
    # # groups in the same index location as the group array
    # groups = []
    # groupmembers = []
    #
    # try:
    #     for row_idx in range(len(samples)):
    #         sample = samples[row_idx]
    #         sample_name = sample[sample_id_col_idx]
    #         curr_group = sample[tissue_group_col_idx]
    #         curr_group_idx = linear_search(curr_group, groups)
    #
    #         if curr_group_idx == -1:
    #             curr_group_idx = len(groups)
    #             groups.append(curr_group)
    #             groupmembers.append([])
    #
    #         groupmembers[curr_group_idx].append(sample_name)
    # except ValueError:
    #     print('Could not assign Sample IDs')
    #
    # # group_counts stores the associated
    # # gene counts for each sample within lists
    # # at the same index position as their groups
    # group_counts = [[] for i in range(len(groups))]
    #
    # version = None
    # dim = None
    # data_header = None
    #
    # gene_name_col = 1
    #
    # try:
    #     for l in gzip.open(data_file_name, 'rt'):
    #         if version is None:
    #             version = l
    #             continue
    #
    #         if dim is None:
    #             dim = [int(x) for x in l.rstrip().split()]
    #             continue
    #
    #         # Sorts the data header so binary_search can be utilized
    #         if data_header is None:
    #             data_header = []
    #             i = 0
    #             for field in l.rstrip().split('\t'):
    #                 data_header.append([field, i])
    #                 i += 1
    #             data_header.sort(key=lambda tup: tup[0])
    #
    #         A = l.rstrip().split('\t')
    #
    #         if A[gene_name_col] == gene_name:
    #             for group_idx in range(len(groups)):
    #                 for member in groupmembers[group_idx]:
    #                     member_idx = binary_search(member, data_header)
    #                     if member_idx != -1:
    #                         group_counts[group_idx].append(int(A[member_idx]))
    #
    #             break
    # except ValueError:
    #     print('Could not read data info file')

    data_viz.boxplot(group_counts, groups,
                     str(args.gene) + ' Expression of Tissue Group',
                     'Tissue Group = ' + str(args.group_type),
                     str(args.gene) + ' Counts', args.output_file)


if __name__ == '__main__':
    main()
