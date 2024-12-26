import json
from faker import Faker

# Initialize Faker
fake = Faker()

# Output file for patients
patients_file_path = "./patients_500000.json"

# Generate 100,000 patient records
patients = []
for _ in range(500_000):
    patients.append({
        "name": fake.name(),
        "dob": str(fake.date_of_birth(minimum_age=6, maximum_age=90)),
        "contact_info": fake.phone_number()
    })

# Save records to JSON
with open(patients_file_path, "w") as file:
    json.dump({"patients": patients}, file, indent=4)

print(f"Generated 500,000 patient records and saved to {patients_file_path}.")
