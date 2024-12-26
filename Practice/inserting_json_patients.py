import requests
import json

BASE_URL = "http://127.0.0.1:8000"
patients_file_path = "./patients_500000.json"

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

# Bulk upload patients
def upload_patients_bulk(token, patients):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/patients/bulk", json={"patients": patients}, headers=headers)
    if response.status_code == 200:
        print(f"Uploaded batch of {len(patients)} patients successfully.")
    else:
        print(f"Failed to upload batch: {response.status_code}, {response.text}")

# Read JSON file and upload in batches
def seed_patients_from_file(token, file_path, batch_size=50000):
    print(f"Seeding patients from {file_path} in batches of {batch_size}...")
    with open(file_path, "r") as file:
        data = json.load(file)
        patients = data["patients"]
    
    for i in range(0, len(patients), batch_size):
        batch = patients[i:i + batch_size]
        upload_patients_bulk(token, batch)
        print(f"Uploaded batch {i // batch_size + 1} of {len(patients) // batch_size}.")
    
    print("Seeding completed!")

if __name__ == "__main__":
    token = authenticate()
    if token:
        seed_patients_from_file(token, patients_file_path)
