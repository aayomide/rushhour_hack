import pytest
from mock_data_generation import (generate_farmer_df, generate_farm_df,
                                  generate_financial_history_df)

class TestFarmerDataFrame:
    @pytest.fixture
    def farmer_df(self):
        return generate_farmer_df()

    def test_farmer_df_null_values(self, farmer_df):
        """Test null values in farmer DataFrame"""
        # Fields that should never be null
        required_fields = [
            'Farmer_ID', 'First Name', 'Last Name', 'Phone Number',
            'Age', 'Gender', 'State of Residence', 'Education_Level',
            'Years_in_Farming', 'Has_Bank_Account', 'Digital_Literacy_Level',
            'Cooperative_Member', 'Agribusiness_Training'
        ]
        for field in required_fields:
            assert not farmer_df[field].isnull().any(), f"Found null values in {field}"

        # Bank details should only be null when Has_Bank_Account is False
        no_account_rows = farmer_df[~farmer_df['Has_Bank_Account']]
        assert no_account_rows['Bank Account'].isnull().all()
        assert no_account_rows['Bank Name'].isnull().all()

    def test_farmer_df_unique_values(self, farmer_df):
        """Test unique constraints in farmer DataFrame"""
        # Farmer_ID should be unique
        assert farmer_df['Farmer_ID'].nunique() == len(farmer_df), "Duplicate Farmer_IDs found"
        
        # Phone numbers should be unique
        assert farmer_df['Phone Number'].nunique() == len(farmer_df), "Duplicate phone numbers found"

class TestFarmDataFrame:
    @pytest.fixture
    def farm_df(self):
        return generate_farm_df()

    def test_farm_df_null_values(self, farm_df):
        """Test null values in farm DataFrame"""
        # All fields in farm DataFrame should be non-null
        assert not farm_df.isnull().any().any(), "Found null values in farm DataFrame"

    def test_farm_df_unique_values(self, farm_df):
        """Test unique constraints in farm DataFrame"""
        # Farm_ID should be unique
        assert farm_df['Farm_ID'].nunique() == len(farm_df), "Duplicate Farm_IDs found"
        
        # Each farmer can have only one farm
        assert farm_df['Farmer_ID'].nunique() == len(farm_df), "Multiple farms per farmer found"

class TestFinancialHistoryDataFrame:
    @pytest.fixture
    def financial_df(self):
        return generate_financial_history_df()

    def test_financial_df_null_values(self, financial_df):
        """Test null values in financial DataFrame"""
        # Fields that should never be null
        required_fields = [
            'Finance_ID', 'Farmer_ID', 'Loan_Purpose', 'Loan_Amount',
            'Interest_Rate', 'Tenure_Months', 'Loan_Approval_Status',
            'Credit Bureau Default_History', 'Source_of_Funding'
        ]
        for field in required_fields:
            assert not financial_df[field].isnull().any(), f"Found null values in {field}"

        # Repayment_Status should be null only for rejected loans
        rejected_loans = financial_df[financial_df['Loan_Approval_Status'] == 'Rejected']
        assert rejected_loans['Repayment_Status'].isnull().all()

    def test_financial_df_unique_values(self, financial_df):
        """Test unique constraints in financial DataFrame"""
        # Finance_ID should be unique
        assert financial_df['Finance_ID'].nunique() == len(financial_df), "Duplicate Finance_IDs found"
        
        # Each farmer should have one loan record
        assert financial_df['Farmer_ID'].nunique() == len(financial_df), "Multiple loans per farmer found"