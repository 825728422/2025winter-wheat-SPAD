# Verification script

The script uses Python 3.10 or newer and pandas. From the package root, run:

```text
python code/verify_subset.py
```

It checks the held-out row-group structure, reports the stage-wise SPAD summary, and records the threshold-sensitivity ranges used in the revision. It does not reconstruct the full field dataset or copy any original raster.
