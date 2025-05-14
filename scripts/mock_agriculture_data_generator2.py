
import pandas as pd
import numpy as np
import random
import uuid
from faker import Faker

fake = Faker()
random.seed(42)
np.random.seed(42)

num_farmers = 3000

# List of Nigerian first and last names
first_names = [
    "Chinedu", "Amina", "Tunde", "Ifeanyi", "Funke",
    "Emeka", "Zainab", "Bayo", "Kemi", "Ibrahim",
    "Uchenna", "Sola", "Ngozi", "Ayoola", "Femi",
    "Adaobi", "Chijioke", "Halima", "Kelechi", "Ijeoma",
    "Segun", "Nneka", "Musa", "Oluchi", "Aishat"
]

# List of 25 random Nigerian last names
last_names = [
    "Okonkwo", "Balogun", "Eze", "Adeyemi", "Nwosu",
    "Ibrahim", "Adebayo", "Obi", "Okafor", "Abubakar",
    "Ogundipe", "Olatunji", "Onwudiwe", "Mohammed", "Ojo",
    "Yusuf", "Umeh", "Alabi", "Ibe", "Ayodele",
    "Ogbonna", "Danjuma", "Okeke", "Adedoyin", "Nwachukwu"
]

def generate_id(prefix):
    return f"{prefix}_{uuid.uuid4().hex[:6]}"

def generate_nigerian_phone_numbers(size):
    # Common Nigerian mobile prefixes
    prefixes = [
        # MTN
        '0803', '0806', '0813', '0816', '0810', '0814', '0903', '0906', '0703', '0706',
        # Airtel
        '0802', '0808', '0812', '0708', '0701', '0902', '0907', '0901', '0912',
        # Glo
        '0805', '0807', '0815', '0811', '0905', '0915',
        # 9mobile
        '0809', '0817', '0818', '0908', '0909',
        # Smile/NTel/Others
        '0704', '0913', '0916', '0918'
    ]

    numbers = []
    for _ in range(size):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices('0123456789', k=7))
        numbers.append(prefix + suffix)

    return numbers

nigerian_states = [
    "Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno",
    "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "FCT", "Gombe", "Imo",
    "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa",
    "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba",
    "Yobe", "Zamfara"
]

# List of common Nigerian banks
nigerian_banks = [
    "Access Bank", "Zenith Bank", "First Bank", "UBA", "GTBank",
    "Fidelity Bank", "Ecobank", "Union Bank", "Stanbic IBTC", "Sterling Bank",
    "Polaris Bank", "FCMB", "Wema Bank", "Jaiz Bank", "Keystone Bank"
]


farmer_ids = [f"FARMER_{str(i+1).zfill(3)}" for i in range(num_farmers)]
first_name = np.random.choice(first_names, size=num_farmers)
last_name = np.random.choice(last_names, size=num_farmers)
phone_numbers = generate_nigerian_phone_numbers(size=num_farmers)
ages = np.random.randint(18, 36, size=num_farmers)
genders = np.random.choice(['Male', 'Female'], size=num_farmers)
state_of_residence = np.random.choice(nigerian_states, size=num_farmers)
# regions = np.random.choice(['North East', 'North West', 'North Central', 'South East', 'South West', 'South South'], size=num_farmers)
education_levels = np.random.choice(['None', 'Primary', 'Secondary', 'Tertiary'], size=num_farmers)
years_in_farming = np.random.randint(1, 15, size=num_farmers)
has_bank_account = np.random.choice([True, False], size=num_farmers, p=[0.70, 0.30])
digital_literacy = np.random.choice(['Low', 'Medium', 'High'], size=num_farmers)
cooperative_member = np.random.choice([True, False], size=num_farmers, p=[0.6, 0.4])
agribusiness_training = np.random.choice([True, False], size=num_farmers, p=[0.55, 0.45])

# Generate bank accounts and bank names (only if farmer has account)
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

dim_farmer = pd.DataFrame({
    'Farmer_ID': farmer_ids,
    'First Name': first_name,
    'Last Name': last_name,
    'Phone Number': phone_numbers,
    'Age': ages,
    'Gender': genders,
    'State of Residence': state_of_residence,
    # 'Region': regions,
    'Education_Level': education_levels,
    'Years_in_Farming': years_in_farming,
    'Has_Bank_Account': has_bank_account,
    'Bank Account': account_numbers,
    'Bank Name': bank_names,
    'Digital_Literacy_Level': digital_literacy,
    'Cooperative_Member': cooperative_member,
    'Agribusiness_Training': agribusiness_training
})

# FARM==============================================================================================================================

# Agriculturally active states
agro_states = [
    "Benue", "Kano", "Kaduna", "Niger", "Taraba", "Plateau",
    "Kebbi", "Sokoto", "Zamfara", "Katsina", "Bauchi",
    "Oyo", "Osun", "Ondo", "Ebonyi", "Cross River"
]

# Farming types
farm_types = ["Crop Farming", "Livestock Farming", "Mixed Farming"]

def generate_farm_locations_and_types(num_farmers):
    farm_locations = []
    crop_types = []

    for _ in range(num_farmers):
        state = random.choice(agro_states)
        farm_type = random.choice(farm_types)

        farm_locations.append(state)
        crop_types.append(farm_type)

    return farm_locations, crop_types

farm_ids = [generate_id("FARM") for _ in range(num_farmers)]
farm_locations, crop_types = generate_farm_locations_and_types(num_farmers)
farm_sizes = np.round(np.random.uniform(1.0, 5.0, size=num_farmers), 2)
irrigation_types = np.random.choice(['None', 'Manual', 'Drip', 'Sprinkler'], size=num_farmers)
# crop_types = np.random.choice(['Maize', 'Cassava', 'Rice', 'Soybeans', 'Tomato', 'Groundnut'], size=num_farmers)
soil_quality = np.random.choice(['Poor', 'Fair', 'Good'], size=num_farmers)
iot_usage = np.random.choice([True, False], size=num_farmers, p=[0.35, 0.65])
market_access = np.random.choice(['Good', 'Poor'], size=num_farmers)
# climate_risk = np.random.choice(['Low', 'Medium', 'High'], size=num_farmers)

# rainfall = np.round(np.random.uniform(500, 2000, size=num_farmers), 2)
pest_incidence = np.random.choice(['Low', 'Moderate', 'High'], size=num_farmers)
weather_anomalies = np.random.choice(['None', 'Frequent', 'Rare'], size=num_farmers)
proximity_to_roads = np.random.choice(['Close', 'Far'], size=num_farmers)
# extension_services = np.random.choice([True, False], size=num_farmers, p=[0.5, 0.5])


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
    # 'Climate_Risk_Level': climate_risk,
    # 'Rainfall_Level': rainfall,
    'Pest_Incidence': pest_incidence,
    'Weather_Anomalies': weather_anomalies,
    'Proximity_to_Roads': proximity_to_roads
})

loan_ids = [generate_id("LOAN") for _ in range(num_farmers)]
loan_purposes = np.random.choice(['Equipment', 'Fertilizer', 'Labor', 'Irrigation', 'Land Expansion'], size=num_farmers)
loan_amounts = np.random.randint(50000, 500000, size=num_farmers)
interest_rates = np.round(np.random.uniform(5.0, 25.0, size=num_farmers), 2)
tenures = np.random.choice([6, 12, 18, 24], size=num_farmers)
default_history = np.random.choice([True, False], size=num_farmers, p=[0.25, 0.75])
funding_sources = np.random.choice(['Bank', 'Microfinance', 'Government', 'NGO'], size=num_farmers)
loan_statuses = np.random.choice(["Approved", "Rejected"], size=num_farmers, p=[0.7, 0.3])
repayment_statuses = []

for status in loan_statuses:
    if status == "Approved":
        repayment = random.choices(["Fully Paid", "Partially Paid", "Defaulted"], weights=[0.5, 0.3, 0.2])[0]
    else:
        repayment = None  # or "" if you prefer empty string
    repayment_statuses.append(repayment)

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

# tech_ids = [generate_id("TECH") for _ in range(num_farmers)]
# mobile_banking = np.random.choice([True, False], size=num_farmers, p=[0.75, 0.25])
# agtech_app = np.random.choice([True, False], size=num_farmers, p=[0.4, 0.6])
# iot_usage = np.random.choice([True, False], size=num_farmers, p=[0.35, 0.65])
# financial_ed = np.random.choice([True, False], size=num_farmers, p=[0.6, 0.4])
# record_keeping = np.random.choice(['None', 'Basic', 'Detailed'], size=num_farmers)

# dim_technology_adoption = pd.DataFrame({
#     'Tech_ID': tech_ids,
#     'Farmer_ID': farmer_ids,
#     'Uses_Mobile_Banking': mobile_banking,
#     'Uses_AgTech_App': agtech_app,
#     'Has_IoT_Sensors': iot_usage,
#     'Participated_in_Financial_Education': financial_ed,
#     'Record_Keeping_Practice': record_keeping
# })

# env_ids = [generate_id("ENV") for _ in range(num_farmers)]
# rainfall = np.round(np.random.uniform(500, 2000, size=num_farmers), 2)
# pest_incidence = np.random.choice(['Low', 'Moderate', 'High'], size=num_farmers)
# weather_anomalies = np.random.choice(['None', 'Frequent', 'Rare'], size=num_farmers)
# proximity_to_roads = np.random.choice(['Close', 'Far'], size=num_farmers)
# extension_services = np.random.choice([True, False], size=num_farmers, p=[0.5, 0.5])

# dim_environmental_factors = pd.DataFrame({
#     'Env_ID': env_ids,
#     'Farm_ID': farm_ids,
#     'Rainfall_Level': rainfall,
#     'Pest_Incidence': pest_incidence,
#     'Weather_Anomalies': weather_anomalies,
#     'Proximity_to_Roads': proximity_to_roads,
#     'Extension_Service_Access': extension_services
# })

# assessment_ids = [generate_id("ASSESS") for _ in range(num_farmers)]
# years = np.random.choice([2021, 2022, 2023], size=num_farmers)
# credit_scores = np.random.randint(300, 850, size=num_farmers)
# repayment_probs = np.round(np.random.uniform(0.3, 0.95, size=num_farmers), 2)
# business_success_probs = np.round(np.random.uniform(0.3, 0.95, size=num_farmers), 2)
# low_risk = (credit_scores > 600) & (repayment_probs > 0.7)

# fact_credit_assessment = pd.DataFrame({
#     'Assessment_ID': assessment_ids,
#     'Farmer_ID': farmer_ids,
#     'Loan_ID': loan_ids,
#     'Year': years,
#     'Credit_Score': credit_scores,
#     'Repayment_Probability': repayment_probs,
#     'Business_Success_Probability': business_success_probs,
#     'Is_Low_Risk': low_risk
# })

# Save all as CSV
dim_farmer.to_csv("dim_farmer2.csv", index=False)
dim_farm.to_csv("dim_farm2.csv", index=False)
dim_financial_history.to_csv("dim_financial_history2.csv", index=False)
# dim_technology_adoption.to_csv("dim_technology_adoption.csv", index=False)
# dim_environmental_factors.to_csv("dim_environmental_factors.csv", index=False)
# fact_credit_assessment.to_csv("fact_credit_assessment.csv", index=False)
