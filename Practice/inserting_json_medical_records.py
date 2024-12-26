import requests
import json

BASE_URL = "http://127.0.0.1:8000"
medical_records_file_path = "./medical_records_500000.json"

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

# Bulk upload medical records
def upload_medical_records_bulk(token, medical_records):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/records/bulk", json={"records": medical_records}, headers=headers)
    if response.status_code == 200:
        print(f"Uploaded batch of {len(medical_records)} medical records successfully.")
    else:
        print(f"Failed to upload batch: {response.status_code}, {response.text}")

# Read JSON file and upload in batches
def seed_medical_records_from_file(token, file_path, batch_size=50000):
    print(f"Seeding medical records from {file_path} in batches of {batch_size}...")
    with open(file_path, "r") as file:
        data = json.load(file)
        medical_records = data["records"]
    
    for i in range(0, len(medical_records), batch_size):
        batch = medical_records[i:i + batch_size]
        upload_medical_records_bulk(token, batch)
        print(f"Uploaded batch {i // batch_size + 1} of {len(medical_records) // batch_size}.")
    
    print("Seeding completed!")

if __name__ == "__main__":
    token = authenticate()
    if token:
        seed_medical_records_from_file(token, medical_records_file_path)
