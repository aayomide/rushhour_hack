from airflow.models import Variable
access_key = Variable.get("access_key")
secret_key = Variable.get("secret_key")
bucket_name = "rushhour-hackathon"
snowflake_table = "agrolift"
farm_path = "dim_farm"
farmer_path = "dim_farmer"
financial_path = "dim_financial"

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

# Agriculturally active states
agro_states = [
    "Benue", "Kano", "Kaduna", "Niger", "Taraba", "Plateau",
    "Kebbi", "Sokoto", "Zamfara", "Katsina", "Bauchi",
    "Oyo", "Osun", "Ondo", "Ebonyi", "Cross River"
]

# Farming types
farm_types = ["Crop Farming", "Livestock Farming", "Mixed Farming"]
