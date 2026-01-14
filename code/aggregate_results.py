import csv
import pandas as pd
# ===============================
# INPUT 
# ===============================

pred_df = pd.read_csv("submission.csv")
# Convert prediction text to numeric score
# consistent -> 1, contradict -> 0
pred_df["score"] = pred_df["prediction"].map({
    "consistent": 1,
    "contradict": 0
})
# ===============================
# AGGREGATION LOGIC
# ===============================

def aggregate_scores(scores):
    """
    Rule:
    If ANY score == 0 → final prediction = 0
    Else → final prediction = 1
    """
    if (scores == 0).any():
        return 0, "At least one narrative chunk contradicts the backstory."
    else:
        return 1, "All narrative chunks are consistent with the backstory."


# ===============================
# WRITE CSV
# ===============================

final_prediction, rationale = aggregate_scores(pred_df["score"])

results_df = pd.DataFrame([{
    "story_id": "story_001",
    "prediction": final_prediction,
    "rationale": rationale
}])

results_df.to_csv("results.csv", index=False)

print("✅ results.csv created successfully")
print(results_df)

