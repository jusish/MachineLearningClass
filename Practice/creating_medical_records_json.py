import json
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Output file for medical records
medical_records_file_path = "./medical_records_500000.json"

# List of sample diagnoses and treatments
diagnoses = [
    "Coronary Artery Disease", "Hypertension", "Diabetes", "Asthma", "Chronic Kidney Disease", 
    "Lung Cancer", "Stroke", "Anemia", "Gastroenteritis", "Hepatitis B", 
    "Chronic Obstructive Pulmonary Disease", "Alzheimer's Disease", "Parkinson's Disease", 
    "Cerebrovascular Accident", "Multiple Sclerosis", "Rheumatoid Arthritis", 
    "Tuberculosis", "Psoriasis", "Obesity", "Hypothyroidism", "Hyperthyroidism", 
    "Chronic Fatigue Syndrome", "Endometriosis", "Polycystic Ovary Syndrome", "Celiac Disease", 
    "Inflammatory Bowel Disease", "Irritable Bowel Syndrome", "Acid Reflux Disease", 
    "Epilepsy", "Septicemia", "HIV/AIDS", "Chronic Migraine", "Obstructive Sleep Apnea", 
    "Cystic Fibrosis", "Huntington's Disease", "Liver Cirrhosis", "Gallbladder Disease", 
    "Chronic Sinusitis", "Asthma Exacerbation", "Gout", "Carpal Tunnel Syndrome", "Lupus", 
    "Bipolar Disorder", "Schizophrenia", "Depression", "Anxiety Disorder", "Post-Traumatic Stress Disorder", 
    "Attention Deficit Hyperactivity Disorder", "Osteoarthritis", "Fibromyalgia", "Sickle Cell Anemia", 
    "Tonsillitis", "Bronchitis", "Pneumonia", "Kidney Stones", "Urinary Tract Infection", 
    "Acute Myocardial Infarction", "Liver Failure", "Acute Pancreatitis", "Cervical Cancer", 
    "Endometrial Cancer", "Breast Cancer", "Prostate Cancer", "Ovarian Cancer", "Colorectal Cancer", 
    "Melanoma", "Leukemia", "Testicular Cancer", "Thyroid Cancer", "Lung Infection"
]


treatments = [
    "Calcium supplements, weight-bearing exercise", "Insulin therapy, glucose monitoring", 
    "Inhalers, bronchodilators", "Diuretics, blood pressure monitoring", "Dialysis, blood pressure meds",
    "Chemotherapy, radiation therapy", "Blood thinners, physiotherapy", "Iron supplements, diet change",
    "Antibiotics, hydration therapy", "Antivirals, rest, hydration", "Oxygen therapy, anti-inflammatory medication", 
    "Physical therapy, muscle relaxants", "Corticosteroids, surgery", "Pain management, physical activity", 
    "Psychotherapy, antidepressants", "Glucose-lowering medications, dietary modifications", 
    "Immunosuppressive drugs, renal transplant", "Chemotherapy, targeted therapy", "Vitamin D supplements, exercise", 
    "Antipsychotics, mood stabilizers", "Surgical resection, chemotherapy", "Physical therapy, pain relief medication", 
    "Surgical intervention, radiation therapy", "Proton therapy, stem cell treatment", "Hormonal therapy, radiation", 
    "Lung transplant, bronchodilators", "Blood transfusions, iron chelation therapy", "Blood pressure medication, lifestyle modification", 
    "Surgical repair, antibiotics", "Dietary modifications, stress management", "Hydration therapy, analgesics", 
    "Radiation therapy, chemotherapy", "Transcranial magnetic stimulation, antidepressants", "Proton pump inhibitors, dietary changes", 
    "Blood sugar management, insulin injections", "Rest, lifestyle changes, medication for symptoms", 
    "Cognitive-behavioral therapy, SSRIs", "Corticosteroids, joint support", "Physical therapy, joint injections", 
    "Surgical excision, chemotherapy", "Anti-inflammatory drugs, surgery", "Tobacco cessation, bronchodilators", 
    "Palliative care, pain management", "Dialysis, kidney transplant", "Opioid analgesics, physiotherapy", 
    "Therapeutic diet, anti-inflammatory drugs", "Surgical resection, physical rehabilitation", "Oxygen supplementation, bronchodilators", 
    "Hydration therapy, electrolyte correction", "Liver transplant, nutritional therapy", "Dietary management, surgery", 
    "Bone marrow transplant, immunotherapy", "Surgical excision, pain management", "Stem cell therapy, physical therapy", 
    "Antiviral treatment, supportive care", "Pain management, spinal injections", "Nutritional therapy, weight management", 
    "Psychiatric support, antidepressant medication"
]


# Generate 500,000 medical records
medical_records = []
for _ in range(500_000):
    medical_records.append({
        "patient_id": random.randint(1, 1500000),  # Random patient ID between 1 and 1,500,000
        "doctor_id": random.randint(1, 6),  # Random doctor ID between 1 and 6
        "diagnosis": random.choice(diagnoses),  # Random diagnosis from predefined list
        "treatment": random.choice(treatments),  # Random treatment from predefined list
        "status": random.choice(["OPEN", "CLOSED"]),  # Random status
    })

# Save records to JSON
with open(medical_records_file_path, "w") as file:
    json.dump({"records": medical_records}, file, indent=4)

print(f"Generated 500,000 medical records and saved to {medical_records_file_path}.")
