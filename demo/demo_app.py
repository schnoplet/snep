from sdk.python.snep_client import SNEPClient

client = SNEPClient()

# Example data
example_data = {
    "meta": {
        "id": "snep://alice.example/recipes/42@v1",
        "publisher": "did:web:alice.example",
        "schema": "snep/recipe/1",
    },
    "data": {
        "title": "Simple Pavlova",
        "ingredients": ["egg whites", "sugar", "cream"],
        "steps": ["whip eggs", "fold sugar", "bake"]
    }
}

# Publish
res = client.publish("recipes", "42", example_data)
print("Published:", res)

# Fetch
fetched = client.fetch("recipes", "42")
print("Fetched:", fetched)

# Verify content hash
hash_local = client.hash_content(fetched["data"])
print("SHA256 hash of fetched data:", hash_local)