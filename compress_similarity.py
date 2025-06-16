import gzip
import pickle

# Compress similarity.pkl to similarity.pkl.gz
with open("similarity.pkl", "rb") as f_in:
    with gzip.open("similarity.pkl.gz", "wb") as f_out:
        f_out.writelines(f_in)

print("✅ similarity.pkl has been compressed successfully to similarity.pkl.gz")
