from sdk.pyclient.snep_client import SNEPClient
from utils.crypto import generate_key, sha256_hash

def main():
    key = generate_key()
    client = SNEPClient(
        key=key,
        node_urls=["http://localhost:5000", "http://localhost:5001"]
    )

    example_data = {"recipe": "pumpkin soup", "steps": ["cut pumpkin", "boil", "blend"]}

    print("Publishing data...")
    res = client.publish("recipes", "42", example_data)
    print("Published:", res)

    print("Fetching data...")
    fetched = client.fetch("recipes", "42")
    print("Fetched:", fetched)

    if fetched:
        print("SHA256 hash of fetched data:", sha256_hash(str(fetched)))

if __name__ == "__main__":
    main()