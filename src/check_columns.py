import pandas as pd

# Load the features file
df = pd.read_csv("outputs/features.csv")

# Print column names
print("✅ Columns found in features.csv:")
print(df.columns.tolist())
