import pandas as pd

# Load chunks
df = pd.read_csv("./data/chunks.csv")

# Query (claim)
query = "Edmond"


# Simple retrieval
results = df[df["chunks"].str.contains(query, case=False, na=False)]

# Print top 5 matches
print(results.head(5))
