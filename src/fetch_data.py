import requests
import time
import os
import json

API_KEY = "cqt_rQ63FVxdtcHGyWfJxqpgdc3Vcb6t"
CHAIN_ID = "1"  # Ethereum Mainnet

def fetch_transactions(wallet):
    url = f"https://api.covalenthq.com/v1/{CHAIN_ID}/address/{wallet}/transactions_v2/"
    params = {"key": API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch: {wallet} | Status: {response.status_code}")
        return None

# Load wallets
with open("data/sample_wallets.txt", "r") as file:

    wallets = [line.strip() for line in file]

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Fetch and save
for wallet in wallets:
    data = fetch_transactions(wallet)
    if data and "data" in data:
        with open(f"data/{wallet}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        print(f"No data for wallet: {wallet}")
    time.sleep(1)
