import requests
import json

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = "first_5_posts.json"

def fetch_posts():
    response = requests.get(API_URL)
    
    # Validate status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    first_five = response.json()[:5]
    
    with open(OUTPUT_FILE, "w") as file:
        json.dump(first_five, file, indent=4)
    
    print(f"Saved first 5 posts to {OUTPUT_FILE}")
    return response.json()
    

def validate_items(items, required_keys, strict=False):    
    required_keys = set(required_keys)
    
    for index, item in enumerate(items):
        item_keys = set(item.keys())
        
        if strict:
            if item_keys != required_keys:
                raise AssertionError(
                    f"Item at index {index} has incorrect keys. "
                    f"Expected: {required_keys}, Got: {item_keys}"
                )
        else:
            if not required_keys.issubset(item_keys):
                raise AssertionError(
                    f"Item at index {index} is missing keys. "
                    f"Missing: {required_keys - item_keys}"
                )

validate_items(fetch_posts(), ["userId", "id", "title", "body"])
    
