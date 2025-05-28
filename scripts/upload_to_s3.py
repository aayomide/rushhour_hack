import pandas as pd
import awswrangler as wr
import logging
from mock_data_generation import (generate_farmer_df, generate_farm_df,
                                    generate_financial_history_df)
from util.config import bucket_name
from util.session import aws_session

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_farmer_parquet(df: pd.DataFrame = None) -> None:
    """
    Save farmer DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Farmer DataFrame to save. If None, uses default.
    """
    logging.info("Saving farmer DataFrame to S3 as Parquet.")
    df = df if df is not None else generate_farmer_df()
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/mock_data/dim_farmer/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )
    logging.info("Farmer DataFrame saved successfully.")


def save_farm_parquet(df: pd.DataFrame = None) -> None:
    """
    Save farm DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Farm DataFrame to save. If None, generates new from farmer IDs.
    """
    logging.info("Saving farm DataFrame to S3 as Parquet.")
    df = df if df is not None else generate_farm_df()
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/mock_data/dim_farm/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )
    logging.info("Farm DataFrame saved successfully.")


def save_financial_parquet(df: pd.DataFrame = None) -> None:
    """
    Save financial history DataFrame to S3 as Parquet.
    
    Args:
        df (pd.DataFrame): Financial history DataFrame to save. If None, generates new from farmer IDs.
    """
    logging.info("Saving financial history DataFrame to S3 as Parquet.")
    df = df if df is not None else generate_financial_history_df()
    wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket_name}/mock_data/dim_financial/",
        boto3_session=aws_session(),
        mode="overwrite",
        dataset=True,
    )
    logging.info("Financial history DataFrame saved successfully.")
