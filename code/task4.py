import pandas as pd

# -----------------------------
# Simple contradiction logic
# -----------------------------
def predict_chunk(text: str) -> str:
    text = text.lower()

    violence_words = [
        "killed", "murdered", "assassinated", "massacred",
        "shot", "stabbed", "burned", "executed"
    ]

    pacifist_words = [
        "pacifist", "avoids violence", "non-violent", "gentle"
    ]

    has_violence = any(w in text for w in violence_words)
    has_pacifism = any(w in text for w in pacifist_words)

    if has_violence and has_pacifism:
        return "contradict"
    else:
        return "consistent"


# -----------------------------
# Main pipeline
# -----------------------------
def generate_submission():
    chunks_df = pd.read_csv("castaways_chunks_2.csv")
    test_df   = pd.read_csv("train.csv")

    # 1. Predict PER CHUNK
    chunk_preds = []
    for _, row in chunks_df.iterrows():
        chunk_preds.append({
            "id": row["id"],
            "prediction": predict_chunk(str(row["text"]))
        })

    pred_df = pd.DataFrame(chunk_preds)

    # 2. Merge with test.csv using ID
    final = test_df.merge(pred_df, on="id", how="left")

    # 3. Safety check
    assert final["prediction"].isna().sum() == 0

    # 4. Save submission
    final[["id", "prediction"]].to_csv(
        "submission.csv", index=False
    )

    print("✅ Submission file created")
    print(final["prediction"].value_counts())


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    generate_submission()
