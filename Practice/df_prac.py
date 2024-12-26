import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:5000"

def get_auth_token():
    """Fetch JWT token for authentication."""
    auth_data = {"username": "justin", "password": "password123"}  # Replace with your password
    try:
        token_response = requests.post(f"{BASE_URL}/token", data=auth_data)
        if token_response.status_code == 200:
            return token_response.json().get("access_token")
        print(f"Failed to get token. Response: {token_response.text}")
    except Exception as e:
        print(f"Error getting token: {str(e)}")
    return None

def fetch_data(endpoint, token):
    """Fetch data from a given API endpoint."""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", headers=headers)
        if response.status_code == 200:
            return pd.DataFrame(response.json())
        print(f"Failed to fetch data from {endpoint}. Response: {response.text}")
    except Exception as e:
        print(f"Error fetching data from {endpoint}: {str(e)}")
    return None

def main():
    token = get_auth_token()
    if not token:
        print("Authentication failed. Exiting...")
        return

    # Step 2: Fetch datasets
    print("Fetching datasets...")
    patients_df = fetch_data("patients", token)
    billing_df = fetch_data("billing", token)

    if patients_df is None or billing_df is None:
        print("Failed to fetch data.")
        return

    # Select the first 20 columns from each DataFrame
    patients_df = patients_df.iloc[:, :20]
    billing_df = billing_df.iloc[:, :20]

    # Merge the DataFrames on 'id' and 'patient_id'
    merged_df = pd.merge(patients_df, billing_df, left_on='id', right_on='patient_id', how='inner')

    # Export merged DataFrame to CSV
    merged_df.to_csv('merged_data.csv', index=False)
    print("Merged data exported to 'merged_data.csv'.")

    # Create separate CSVs for name & dob and contact_info
    name_dob_df = patients_df[['name', 'dob']]
    name_dob_df.to_csv('name_dob.csv', index=False)
    print("Name and DOB exported to 'name_dob.csv'.")

    contact_info_df = patients_df[['contact_info']]
    contact_info_df.to_csv('contact_info.csv', index=False)
    print("Contact info exported to 'contact_info.csv'.")

    # Concatenate name_dob.csv and contact_info.csv
    concatenated_df = pd.concat([name_dob_df, contact_info_df], axis=1)  # Concatenate along columns
    concatenated_df.to_csv('name_dob_contact_info.csv', index=False)
    print("Concatenated name and DOB with contact info exported to 'name_dob_contact_info.csv'.")

if __name__ == "__main__":
    main()