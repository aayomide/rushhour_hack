import logging
import pandas as pd
import numpy as np
import random
import uuid
from faker import Faker
from util.config import (first_names, last_names, nigerian_states, num_farmers,
                         nigerian_banks, agro_states, farm_types, prefixes)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
fake = Faker()
random.seed(42)
np.random.seed(42)

def generate_id(prefixes: str) -> str:
    """Generate a unique ID with a given prefix."""
    return f"{prefixes}_{uuid.uuid4().hex[:6]}"

def generate_nigerian_phone_numbers(size: int) -> list[str]:
    """Generate a list of Nigerian phone numbers."""
    numbers = []
    for _ in range(size):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=7))
        numbers.append(prefix + suffix)
    return numbers

def generate_farmer_df():
    """
    Generate and return the farmer DataFrame.
    
    Args:
        num_farmers (int): Number of farmer records to generate. Defaults to 3000.
    
    Returns:
        pd.DataFrame: DataFrame containing farmer information with columns:
            - Farmer_ID (str): Unique identifier for each farmer
            - First Name (str): Farmer's first name
            - Last Name (str): Farmer's last name
            - Phone Number (str): Nigerian phone number
            - Age (int): Age between 18-36
            - Gender (str): Male or Female
            - State of Residence (str): Nigerian state
            - Education_Level (str): None/Primary/Secondary/Tertiary
            - Years_in_Farming (int): Years of farming experience
            - Has_Bank_Account (bool): Whether farmer has a bank account
            - Bank Account (str): 10-digit account number if has account
            - Bank Name (str): Name of bank if has account
            - Digital_Literacy_Level (str): Low/Medium/High
            - Cooperative_Member (bool): Whether part of cooperative
            - Agribusiness_Training (bool): Whether received training
    """
    try:
        logging.info("Generating farmer DataFrame...")
        farmer_ids = [f"FARMER_{str(i+1).zfill(3)}" for i in range(num_farmers)]
        first_name = np.random.choice(first_names, size=num_farmers)
        last_name = np.random.choice(last_names, size=num_farmers)
        phone_numbers = generate_nigerian_phone_numbers(size=num_farmers)
        ages = np.random.randint(18, 36, size=num_farmers)
        genders = np.random.choice(['Male', 'Female'], size=num_farmers)
        state_of_residence = np.random.choice(nigerian_states, size=num_farmers)
        education_levels = np.random.choice(['None', 'Primary', 'Secondary', 'Tertiary'], size=num_farmers)
        years_in_farming = np.random.randint(1, 15, size=num_farmers)
        has_bank_account = np.random.choice([True, False], size=num_farmers, p=[0.70, 0.30])
        digital_literacy = np.random.choice(['Low', 'Medium', 'High'], size=num_farmers)
        cooperative_member = np.random.choice([True, False], size=num_farmers, p=[0.6, 0.4])
        agribusiness_training = np.random.choice([True, False], size=num_farmers, p=[0.55, 0.45])

        account_numbers = []
        bank_names = []
        for has_account in has_bank_account:
            if has_account:
                account_number = ''.join(random.choices('0123456789', k=10))
                bank = random.choice(nigerian_banks)
            else:
                account_number = np.nan
                bank = np.nan
            account_numbers.append(account_number)
            bank_names.append(bank)
        logging.info("parsing as a DataFrame.")
        dim_farmer =  pd.DataFrame({
            'Farmer_ID': farmer_ids,
            'First Name': first_name,
            'Last Name': last_name,
            'Phone Number': phone_numbers,
            'Age': ages,
            'Gender': genders,
            'State of Residence': state_of_residence,
            'Education_Level': education_levels,
            'Years_in_Farming': years_in_farming,
            'Has_Bank_Account': has_bank_account,
            'Bank Account': account_numbers,
            'Bank Name': bank_names,
            'Digital_Literacy_Level': digital_literacy,
            'Cooperative_Member': cooperative_member,
            'Agribusiness_Training': agribusiness_training
        })
        logging.info("parsing DataFrame completed data generated successfully.")
        return dim_farmer
    except Exception as e:
        raise Exception(f"Error generating farmer DataFrame: {str(e)}")
       
def generate_farm_df():
    """
    Generate and return the farm DataFrame.
    
    Args:
        num_farmers (int): Number of farm records to generate. Defaults to 3000.
    
    Returns:
        pd.DataFrame: DataFrame containing farm information with columns:
            - Farm_ID (str): Unique identifier for each farm
            - Farmer_ID (str): ID of farmer who owns the farm
            - Farm_Location (str): State where farm is located
            - Farm_Size (float): Size in hectares (1.0-5.0)
            - Irrigation_Type (str): None/Manual/Drip/Sprinkler
            - Crop_Type (str): Type of farming
            - Has_IoT_Sensors (bool): Whether farm uses IoT
            - Soil_Quality (str): Poor/Fair/Good
            - Access_to_Market (str): Good/Poor
            - Pest_Incidence (str): Low/Moderate/High
            - Weather_Anomalies (str): None/Frequent/Rare
            - Proximity_to_Roads (str): Close/Far
    """
    try:
        logging.info("Generating farm DataFrame...")
        farm_ids = [generate_id("FARM") for _ in range(num_farmers)]
        farmer_ids = [f"FARMER_{str(i+1).zfill(3)}" for i in range(num_farmers)]
        farm_locations = [random.choice(agro_states) for _ in range(num_farmers)]
        crop_types = [random.choice(farm_types) for _ in range(num_farmers)]
        farm_sizes = np.round(np.random.uniform(1.0, 5.0, size=num_farmers), 2)
        irrigation_types = np.random.choice(['None', 'Manual', 'Drip', 'Sprinkler'], size=num_farmers)
        soil_quality = np.random.choice(['Poor', 'Fair', 'Good'], size=num_farmers)
        iot_usage = np.random.choice([True, False], size=num_farmers, p=[0.35, 0.65])
        market_access = np.random.choice(['Good', 'Poor'], size=num_farmers)
        pest_incidence = np.random.choice(['Low', 'Moderate', 'High'], size=num_farmers)
        weather_anomalies = np.random.choice(['None', 'Frequent', 'Rare'], size=num_farmers)
        proximity_to_roads = np.random.choice(['Close', 'Far'], size=num_farmers)

        logging.info("parsing as a DataFrame.")
        dim_farm = pd.DataFrame({
            'Farm_ID': farm_ids,
            'Farmer_ID': farmer_ids,
            'Farm_Location': farm_locations,
            'Farm_Size': farm_sizes,
            'Irrigation_Type': irrigation_types,
            'Crop_Type': crop_types,
            'Has_IoT_Sensors': iot_usage,
            'Soil_Quality': soil_quality,
            'Access_to_Market': market_access,
            'Pest_Incidence': pest_incidence,
            'Weather_Anomalies': weather_anomalies,
            'Proximity_to_Roads': proximity_to_roads
        })
        logging.info("parsing DataFrame completed data generated successfully.")
        return dim_farm
    except Exception as e:
        raise Exception(f"Error generating farm DataFrame: {str(e)}")


def generate_financial_history_df():
    """
    Generate and return the financial history DataFrame.
    
    Args:
        num_farmers (int): Number of financial records to generate. Defaults to 3000.
    
    Returns:
        pd.DataFrame: DataFrame containing financial information with columns:
            - Finance_ID (str): Unique identifier for each loan
            - Farmer_ID (str): ID of farmer who took the loan
            - Loan_Purpose (str): Purpose of loan
            - Loan_Amount (int): Amount between 50,000-500,000
            - Interest_Rate (float): Rate between 5.0-25.0
            - Tenure_Months (int): 6/12/18/24 months
            - Loan_Approval_Status (str): Approved/Rejected
            - Repayment_Status (str): Fully Paid/Partially Paid/Defaulted/None
            - Credit Bureau Default_History (bool): Previous default history
            - Source_of_Funding (str): Bank/Microfinance/Government/NGO
    """
    try:
        logging.info("Generating financial history DataFrame...")
        loan_ids = [generate_id("LOAN") for _ in range(num_farmers)]
        farmer_ids = [f"FARMER_{str(i+1).zfill(3)}" for i in range(num_farmers)]
        loan_purposes = np.random.choice(['Equipment', 'Fertilizer', 'Labor', 'Irrigation', 'Land Expansion'], size=num_farmers)
        loan_amounts = np.random.randint(50000, 500000, size=num_farmers)
        interest_rates = np.round(np.random.uniform(5.0, 25.0, size=num_farmers), 2)
        tenures = np.random.choice([6, 12, 18, 24], size=num_farmers)
        default_history = np.random.choice([True, False], size=num_farmers, p=[0.25, 0.75])
        funding_sources = np.random.choice(['Bank', 'Microfinance', 'Government', 'NGO'], size=num_farmers)
        loan_statuses = np.random.choice(["Approved", "Rejected"], size=num_farmers, p=[0.7, 0.3])
        repayment_statuses = [
            random.choices(["Fully Paid", "Partially Paid", "Defaulted"], weights=[0.5, 0.3, 0.2])[0]
            if status == "Approved" else None
            for status in loan_statuses
        ]
        logging.info("parsing as a DataFrame.")
        dim_financial_history = pd.DataFrame({
            'Finance_ID': loan_ids,
            'Farmer_ID': farmer_ids,
            'Loan_Purpose': loan_purposes,
            'Loan_Amount': loan_amounts,
            'Interest_Rate': interest_rates,
            'Tenure_Months': tenures,
            'Loan_Approval_Status': loan_statuses,
            'Repayment_Status': repayment_statuses,
            'Credit Bureau Default_History': default_history,
            'Source_of_Funding': funding_sources
        })
        logging.info("parsing DataFrame completed data generated successfully.")   
        return dim_financial_history
    except Exception as e:
        raise Exception(f"Error generating financial history DataFrame: {str(e)}")
