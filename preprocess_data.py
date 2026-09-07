import h5py
import numpy as np

def clean_rare_h5(input_file, output_file):
    with h5py.File(input_file, "r") as f:
        X = f["data"][:]              # cell x gene
        label = f["label"][:]
        gene_name = f["gene_name"][:]
        cell = f["cell"][:]

    print("Input:", input_file)
    print("Original shape:", X.shape)

    if X.shape[0] != len(cell) or X.shape[1] != len(gene_name):
        raise ValueError("The data matrix must have shape: cell x gene.")

    expressed_cell_num = np.count_nonzero(X > 0, axis=0)
    keep_gene = expressed_cell_num >= 2

    X_clean = X[:, keep_gene]
    gene_name_clean = gene_name[keep_gene]

    print("Genes expressed in 0 cells:", np.sum(expressed_cell_num == 0))
    print("Genes expressed in 1 cell:", np.sum(expressed_cell_num == 1))
    print("Filtered shape:", X_clean.shape)

    with h5py.File(output_file, "w") as f:
        f.create_dataset("data", data=X_clean, compression="gzip", compression_opts=6)
        f.create_dataset("label", data=label)
        f.create_dataset("gene_name", data=gene_name_clean)
        f.create_dataset("cell", data=cell)

    print("Saved:", output_file)


clean_rare_h5(
    "/media/swust123/DATA1/qiu_data/project/real_data/New2/filter/data/rare.h5",
    "/media/swust123/DATA1/qiu_data/project/real_data/filter/rare_clean.h5"
)