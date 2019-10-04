conda install pycodestyle

test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run python plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png
assert_no_stdout

run pycodestyle plot_gtex.py
assert_no_stdout
assert_no_stderr