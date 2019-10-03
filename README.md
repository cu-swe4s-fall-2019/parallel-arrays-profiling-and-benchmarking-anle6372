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

## data_viz.py
    1. Copied data_viz.py and testing framework test_data_viz.py
    2. Eliminated use of math_lib and associated tests
    3. Added multiple dataset input functionality for boxplotting
    4. Added tests to catch incorrect nested list input

## plot_gtex.py
    1. linear_search():
        - Created testing file test_linear_search():
        - Added input testing to ensure list
        - Added input testing to ensure key and list elements are same type
        - Added linear search functionality
        - Enabled full type and gene expression plot capibilities
        - Benchmarking using GNU time yielded 128.18 seconds and used 139768 kB

Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

