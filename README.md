# Partial reproducibility package for agriculture-4652820

This package supports verification of the workflow reported in the revised manuscript. It contains:

- a processed held-out row-group subset (`data/heldout_row_group_R1.csv`, 200 plot-date records);
- the fixed-RF grain-filling mask-sensitivity table (`data/mask_sensitivity_GF.csv`), containing 31 threshold alternatives without the booting extent plus one extent-based reconstruction;
- a data dictionary and model settings;
- five low-resolution RGB examples from one plot, one per flight date; and
- a small verification script that checks the subset and writes a stage-wise summary.

The subset is provided for peer-review verification and is not the complete field dataset. The package supports checks of the supplied subset and reported processing summaries; it cannot reproduce the complete analysis. The extent-based row in the sensitivity table is an independent reconstruction rather than an exact replication of the original mask-transfer operation. Original high-resolution UAV imagery and other raw project files are not included. The complete dataset and original imagery will be considered for release after acceptance, subject to author and project permissions.


## Quick check

```text
python code/verify_subset.py
```

The reported workflow uses four reflectance bands and 15 vegetation indices. The reference RF uses 500 trees, square-root feature sampling, minimum leaf size 2 and random seed 20261002. The study validation is leave-one-row-group-out with grouped inner tuning.
