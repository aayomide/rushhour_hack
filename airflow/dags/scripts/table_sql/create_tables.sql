CREATE TABLE  IF NOT EXISTS dim_farmers (
    Farmer_ID STRING PRIMARY KEY,
    First_Name STRING,
    Last_Name STRING,
    Phone_Number STRING,
    Age INTEGER,
    Gender STRING,
    State_of_Residence STRING,
    Education_Level STRING,
    Years_in_Farming INTEGER,
    Has_Bank_Account BOOLEAN,
    Bank_Account STRING,
    Bank_Name STRING,
    Digital_Literacy_Level STRING,
    Cooperative_Member BOOLEAN,
    Agribusiness_Training BOOLEAN
);

CREATE TABLE IF NOT EXISTS dim_farms (
    Farm_ID STRING PRIMARY KEY,
    Farmer_ID STRING,
    Farm_Location STRING,
    Farm_Size FLOAT,
    Irrigation_Type STRING,
    Crop_Type STRING,
    Has_IoT_Sensors BOOLEAN,
    Soil_Quality STRING,
    Access_to_Market STRING,
    Pest_Incidence STRING,
    Weather_Anomalies STRING,
    Proximity_to_Roads STRING
);

CREATE TABLE IF NOT EXISTS dim_financials (
    Finance_ID STRING PRIMARY KEY,
    Farmer_ID STRING,
    Loan_Purpose STRING,
    Loan_Amount INTEGER,
    Interest_Rate FLOAT,
    Tenure_Months INTEGER,
    Loan_Approval_Status STRING,
    Repayment_Status STRING,
    Credit_Bureau_Default_History BOOLEAN,
    Source_of_Funding STRING
);
