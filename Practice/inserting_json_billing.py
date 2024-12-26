import requests
import json

BASE_URL = "http://127.0.0.1:8000"
billing_file_path = "./billing_500000.json"

# Authenticate to get the access token
def authenticate():
    login_data = {
        "username": "justin",  # Replace with actual username
        "password": "password123"  # Replace with actual password
    }
    response = requests.post(f"{BASE_URL}/token", data=login_data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to authenticate: {response.status_code}, {response.text}")
        return None

# Bulk upload billing records
def upload_billing_bulk(token, billing_records):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/billing/bulk", json={"records": billing_records}, headers=headers)
    if response.status_code == 200:
        print(f"Uploaded batch of {len(billing_records)} billing records successfully.")
    else:
        print(f"Failed to upload batch: {response.status_code}, {response.text}")

# Read JSON file and upload in batches
def seed_billing_from_file(token, file_path, batch_size=50000):
    print(f"Seeding billing records from {file_path} in batches of {batch_size}...")
    with open(file_path, "r") as file:
        data = json.load(file)
        billing_records = data["records"]
    
    for i in range(0, len(billing_records), batch_size):
        batch = billing_records[i:i + batch_size]
        upload_billing_bulk(token, batch)
        print(f"Uploaded batch {i // batch_size + 1} of {len(billing_records) // batch_size}.")
    
    print("Seeding completed!")

if __name__ == "__main__":
    token = authenticate()
    if token:
        seed_billing_from_file(token, billing_file_path)
