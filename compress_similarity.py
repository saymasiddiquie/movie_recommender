import gzip
import shutil

with open("similarity.pkl", "rb") as f_in:
    with gzip.open("similarity.pkl.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print("Compression completed. File saved as similarity.pkl.gz")

