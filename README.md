# CoSTA

CoSTA is a two-stage framework for sparse single-cell RNA sequencing (scRNA-seq) expression recovery. The provided `main.py` implements the complete CoSTA imputation workflow, including preprocessing, contrastive representation learning, neighborhood construction, neighborhood-aware decoding, and expression reconstruction.

## Environment

The code was run with:

- Python 3.12.9
- CUDA 12.8
- h5py 3.13.0
- NumPy 2.2.6
- SciPy 1.15.2
- scikit-learn 1.6.1
- PyTorch 2.8.0.dev20250526+cu128

The Python dependencies are listed in `requirements.txt`.

## Input data

The input is an HDF5 (`.h5`) file. The expression matrix is stored under `data` in gene-by-cell orientation. The following metadata fields are supported when available:

- `gene_name`: gene names
- `cell`: cell identifiers
- `label`: cell-type labels
- `time`: temporal information
- `batch_label`: batch labels

## Running CoSTA

Set the input and output paths at the beginning of `main.py`:

```python
INPUT_H5_PATH = "/path/to/input.h5"
OUTPUT_H5_PATH = "/path/to/output.h5"
```

Then run:

```bash
python main.py
```

GPU execution is enabled by default. The GPU ID can be changed in the program entry point if necessary.

## Reproducibility

The random seed is fixed to `24` in `main.py`. Random seeds are set for Python, NumPy, PyTorch, and CUDA, and deterministic cuDNN behavior is enabled.

## Output

The reconstructed expression matrix is written to the `data` dataset of the output HDF5 file. Available gene, cell, label, time, and batch metadata are also copied to the output file.

The reconstructed values are transformed from normalized log1p space back to the original expression scale. Negative values after inverse transformation are clipped to zero, while originally observed nonzero entries are retained.

## Files

```text
CoSTA_release/
├── main.py
├── requirements.txt
└── README.md
```

`main.py` contains the CoSTA imputation workflow, and `requirements.txt` contains the third-party Python packages directly imported by this script.
