import random
import json
# Generate realistic medical records data
diagnoses = [
    "Type 2 Diabetes", "Hypertension", "Migraine", "Asthma", "Depression",
    "Allergic Rhinitis", "Arthritis", "Gastroesophageal Reflux Disease", "Chronic Bronchitis", "Epilepsy",
    "Hyperlipidemia", "Hypothyroidism", "Psoriasis", "Coronary Artery Disease", "Osteoporosis"
]

treatments = [
    "Metformin 500mg daily, diet control, regular exercise",
    "Lisinopril 10mg daily, low sodium diet",
    "Sumatriptan as needed, stress management",
    "Albuterol Inhaler as needed, avoid allergens",
    "Sertraline 50mg daily, psychotherapy sessions",
    "Antihistamines, nasal sprays, avoid triggers",
    "Ibuprofen 400mg as needed, physical therapy",
    "Omeprazole 20mg daily, avoid spicy foods",
    "Bronchodilators, regular pulmonary checkups",
    "Anti-epileptic medications, regular EEG monitoring",
    "Statins, dietary modifications",
    "Levothyroxine 50mcg daily, regular TSH checks",
    "Topical corticosteroids, UV light therapy",
    "Aspirin 75mg daily, lifestyle changes",
    "Calcium supplements, weight-bearing exercise"
]

statuses = ["OPEN", "FOLLOW_UP", "CLOSED"]

medical_records = []
for i in range(1, 301):  # 300 entries
    patient_id = random.randint(1, 300)
    doctor_id = random.randint(1, 6)
    diagnosis = random.choice(diagnoses)
    treatment = random.choice(treatments)
    status = random.choice(statuses)
    medical_records.append({
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": diagnosis,
        "treatment": treatment,
        "status": status
    })

medical_records_data = {"records": medical_records}
medical_records_file_path = "./realistic_medical_records_300.json"

with open(medical_records_file_path, "w") as file:
    json.dump(medical_records_data, file, indent=4)

# Billing Records
billing_records = []
for i in range(1, 301):  # 300 entries
    patient_id = random.randint(1, 300)
    total_cost = round(random.uniform(50.0, 500.0), 2)  # Random cost between 50 and 500
    billing_records.append({
        "patient_id": patient_id,
        "total_cost": total_cost
    })

billing_records_data = {"records": billing_records}
billing_records_file_path = "./realistic_billing_records_300.json"

with open(billing_records_file_path, "w") as file:
    json.dump(billing_records_data, file, indent=4)

medical_records_file_path, billing_records_file_path