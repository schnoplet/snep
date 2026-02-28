from sdk.python.snep_client import SNEPClient
from utils.crypto import generate_key, sha256_hash

def main():
    key = generate_key()

    # SNEP client pointing to node1
    client = SNEPClient(
        key=key,
        node_urls=["http://localhost:5000", "http://localhost:5001"]
    )

    example_data = {
        "recipe": "pumpkin soup",
        "steps": ["cut pumpkin", "boil", "blend"]
    }

    # publish to nodes
    res = client.publish("recipes", "42", example_data)
    print("Published:", res)

    # fetch from node1
    fetched1 = client.fetch_from_node("http://localhost:5000", "recipes", "42")
    print("Fetched from node1:", fetched1)
    print("SHA256 node1:", sha256_hash(str(fetched1)))

    # fetch from node2
    fetched2 = client.fetch_from_node("http://localhost:5001", "recipes", "42")
    print("Fetched from node2:", fetched2)
    print("SHA256 node2:", sha256_hash(str(fetched2)))

if __name__ == "__main__":
    main()