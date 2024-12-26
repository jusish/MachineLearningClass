import requests
import random
from faker import Faker

BASE_URL = "http://127.0.0.1:5000"
fake = Faker()

# Constants for sample data
DOCTORS = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Taylor"]
CONDITIONS = ["Flu", "Cold", "COVID-19", "Asthma", "Diabetes"]

# Total rows target
PATIENTS_COUNT = 70_000
BILLING_COUNT = 500_000

# Authenticate to get token
def authenticate():
    login_data = {
        "username": "justin",  # Replace with actual username
        "password": "password123"   # Replace with actual password
    }

    response = requests.post(f"{BASE_URL}/token", data=login_data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to authenticate: {response.status_code}, {response.text}")
        return None

# Use the token for authenticated requests
def create_billing_record(token, patient_id):
    headers = {"Authorization": f"Bearer {token}"}
    
    # Fake billing data
    total_cost = round(random.uniform(50.0, 500.0), 2)  # Random total cost between 50 and 500

    data = {
        "patient_id": patient_id,
        "total_cost": total_cost,
    }

    response = requests.post(f"{BASE_URL}/billing/", json=data, headers=headers)
    if response.status_code == 200:
        print(f"Created billing record for patient ID: {patient_id} with cost: {total_cost}")
    else:
        print(f"Failed to create billing record: {response.status_code}, Response Text: {response.text}")

# Main function to seed billing data
def seed_billing_data(token):
    print("Seeding billing data...")

    # You may want to fetch a list of patient_ids from your database or use a range for simulation
    patient_ids = range(1, PATIENTS_COUNT + 1)  # Simulating patient IDs from 1 to 200,000

    for _ in range(BILLING_COUNT):
        patient_id = random.choice(patient_ids)  # Randomly choose a patient ID for billing
        create_billing_record(token, patient_id)

    print("Seeding completed!")

if __name__ == "__main__":
    token = authenticate()
    if token:
        seed_billing_data(token)
