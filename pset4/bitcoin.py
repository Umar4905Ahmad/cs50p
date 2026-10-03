import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0f3c1d3effc6c4aa8bb3a457e941552efb348197de2a7ba0dca27d7a58658b71")
except requests.RequestException:
    sys.exit("Request failed")

data = response.json()
price = float(data["data"]["priceUsd"])

print(f"${n * price:,.4f}")