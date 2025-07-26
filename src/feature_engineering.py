import json
import os
import pandas as pd

input_folder = "data"
output_file = "outputs/features.csv"

features = []

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(input_folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                transactions = data.get("data", {}).get("items", [])
                
                num_tx = len(transactions)
                total_gas = sum(tx.get("gas_spent", 0) for tx in transactions)
                max_value = max([tx.get("value", 0) for tx in transactions], default=0)

                features.append({
                    "wallet_id": filename.replace(".json", ""),
                    "num_transactions": num_tx,
                    "total_gas_spent": total_gas,
                    "max_transaction_value": max_value
                })
            except json.JSONDecodeError:
                print(f"Invalid JSON in {filename}, skipping.")

# Save to CSV
df = pd.DataFrame(features)
df.to_csv(output_file, index=False)
print(f"Saved features for {len(df)} wallets to {output_file}")
