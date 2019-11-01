# parallel-arrays-profiling-and-benchmarking

## Operation

    1. Activate conda

```
conda activate swe4s
```
    2. Install matplotlib

```
conda install matplotlib
```
    3. Run in command line
```
$ python plot_gtex.py \
--gene_reads
GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz \
--sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt \
--gene ACTA2 \
--group_type SMTS \
--output_file ACTA2.png
```

## data_viz.py
    1. Copied data_viz.py and testing framework test_data_viz.py
    2. Eliminated use of math_lib and associated tests
    3. Added multiple dataset input functionality for boxplotting
    4. Added tests to catch incorrect nested list input

## plot_gtex.py
    1. linear_search():
        - Created testing file test_plot_gtex.py
        - Added input testing to ensure list
        - Added input testing to ensure key and list elements are same type
        - Added linear search functionality
        - Enabled full type and gene expression plot capibilities

    2. binary_search():
        - Added binary searching functionality
        - Added testing for presence/absence of created files
        - Added simple functional testing with Stupid Simple Bash Testing

## Profiling and Benchmarking Results:

    1. linear_search():
        - Profiling using cProfile showed that linear_search(): was the largest time user
            + cProfile results can be viewed in flie: plot_gtex.linear_search.txt
        - Benchmarking using GNU time yielded 128.18 seconds and used 139768 kB
    
    2. binary_search():
        - Benchmarking using GNU time yielded 1.02 seconds and used 142400 kB
    3. Hash Table Implementation:
        - Benchmarking using GNU time yielded 1.96 seconds and used 147188
        - Noted that this is not significantly better than binary search!!

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

