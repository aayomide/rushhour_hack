import pandas as pd
import awswrangler as wr
from mock_data_generation import generate_farmer_df, generate_farm_df, generate_financial_history_df
from config import bucket_name
from session import aws_session

def save_farmer_parquet(df: pd.DataFrame = None) -> None:
    """
    Save farmer DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Farmer DataFrame to save. If None, uses default.
    """
    df = df if df is not None else generate_farmer_df(num_farmers=3000)
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/dim_farmer/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )

def save_farm_parquet(df: pd.DataFrame = None) -> None:
    """
    Save farm DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Farm DataFrame to save. If None, generates new from farmer IDs.
    """
    df = df if df is not None else generate_farm_df(num_farmers=3000, farmer_ids=farmers_df['Farmer_ID'].tolist())
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/dim_farm/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )

def save_financial_parquet(df: pd.DataFrame = None) -> None:
    """
    Save financial history DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Financial history DataFrame to save. If None, generates new from farmer IDs.
    """
    df = df if df is not None else generate_financial_history_df(num_farmers=3000, farmer_ids=farmers_df['Farmer_ID'].tolist())
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/dim_financial/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )