import pandas as pd

# Load the engineered features
df = pd.read_csv("outputs/features.csv")

# Normalize and calculate score
df["score"] = (
    0.4 * df["num_transactions"].rank(pct=True) +
    0.3 * df["total_gas_spent"].rank(pct=True) +
    0.3 * df["max_transaction_value"].rank(pct=True)
) * 1000

# Convert scores to integer
df["score"] = df["score"].astype(int)

# Save final scores
df[["wallet_id", "score"]].to_csv("outputs/wallet_scores.csv", index=False)
print("✅ Saved scores to outputs/wallet_scores.csv")
