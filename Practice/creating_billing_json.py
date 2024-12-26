import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Output file for patients
billing_file_path = "./billing_500000.json"

# Generate 100,000 patient records
billing = []
for _ in range(500_000):
    billing.append({
        "patient_id": random.randint(0, 400000),
        "total_cost": round(random.uniform(50.0, 12500.0), 2)
    })

# Save records to JSON
with open(billing_file_path, "w") as file:
    json.dump({"records": billing}, file, indent=4)

print(f"Generated 500,000 patient records and saved to {billing_file_path}.")
