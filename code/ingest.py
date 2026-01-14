import pathway as pw

table = pw.io.fs.read(
    "./data",
    format="plaintext"
)

pw.debug.compute_and_print(table, include_id=False)
