import pathway as pw

# 1️⃣ Read text files
table = pw.io.fs.read(
    "./data",
    format="plaintext",
    mode="static"
)

# 2️⃣ Chunking function
@pw.udf
def chunk_text(text: str, chunk_size: int = 200):
    words = text.split()
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]

# 3️⃣ Apply chunking
chunked = table.select(
    chunks=chunk_text(table.data)
)

# 4️⃣ Flatten chunks
flattened = chunked.flatten(chunked.chunks)

# 5️⃣ Save to CSV (Pathway way)
pw.io.csv.write(
    flattened,
    "./data/chunks.csv"
)

pw.run()
