import requests
import random
from faker import Faker

BASE_URL = "http://127.0.0.1:5000"
fake = Faker()

# Constants for sample data
DOCTORS = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Brown", "Dr. Taylor"]
CONDITIONS = ["Flu", "Cold", "COVID-19", "Asthma", "Diabetes"]

# Total rows target
TOTAL_ROWS = 500_000
PATIENTS_COUNT = 500_000
BILLING_COUNT = 500_000
MEDICAL_RECORDS_COUNT = 500_000

# Authenticate to get token
def authenticate():
    login_data = {
        "username": "justin",  # Replace with actual username
        "password": "password123"   # Replace with actual password
    }

    # Ensure that you're using the correct format for FastAPI's OAuth2 flow
    response = requests.post(f"{BASE_URL}/token", data=login_data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to authenticate: {response.status_code}, {response.text}")
        return None

# Use the token for authenticated requests
def create_patient(token):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": fake.name(),
        "dob": str(fake.date_of_birth(minimum_age=18, maximum_age=90)),
        "contact_info": fake.phone_number()
    }
    response = requests.post(f"{BASE_URL}/patients/", json=data, headers=headers)
    if response.status_code == 200:
        print(f"Created patient: {data['name']}")
    else:
        print(f"Failed to create patient: {response.status_code}, Response Text: {response.text}")

# Main function to seed data
def seed_data(token):
    print("Seeding data...")

    for _ in range(PATIENTS_COUNT):
        create_patient(token)

    print("Seeding completed!")

if __name__ == "__main__":
    token = authenticate()
    if token:
        seed_data(token)
