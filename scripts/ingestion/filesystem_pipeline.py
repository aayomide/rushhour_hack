import os
from typing import Iterator

import dlt
from dlt.sources import TDataItems
from dlt.sources.filesystem import FileItemDict, filesystem, readers, read_csv


# where the test files are, those examples work with (url)
TESTS_BUCKET_URL = "aws_s3_bucket_path"


def farm_merge() -> None:
    """
    Loads and merges farm data from parquet files into Snowflake.

    The function reads parquet files from S3, configures merge settings using farm_id
    as the merge key, and loads the data into the agrolift_schema in Snowflake.

    Returns:
        None
    """
    pipeline = dlt.pipeline(
        pipeline_name="farm",
        destination='snowflake',
        dataset_name="agrolift_schema",
    )
    
    farm_files = readers(bucket_url=TESTS_BUCKET_URL, file_glob="mock_data/dim_farm/*.parquet").read_parquet()
    farm_files.apply_hints(write_disposition="merge", merge_key="farm_id")

    load_info = pipeline.run(farm_files.with_name("dim_farms"))
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)


def farmers_merge() -> None:
    """Loads and merges farmer data from parquet files into Snowflake.

    The function reads parquet files from S3, configures merge settings using farmer_id
    as the merge key, and loads the data into the agrolift_schema in Snowflake.

    Returns:
        None
    """
    pipeline = dlt.pipeline(
        pipeline_name="farmer",
        destination='snowflake',
        dataset_name="agrolift_schema",
    )
    
    farmer_files = readers(bucket_url=TESTS_BUCKET_URL, file_glob="mock_data/dim_farmer/*.parquet").read_parquet()
    farmer_files.apply_hints(write_disposition="merge", merge_key="farmer_id")

    load_info = pipeline.run(farmer_files.with_name("dim_farmers"))
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)


def financial_merge() -> None:
    """Loads and merges financial data from parquet files into Snowflake.

    The function reads parquet files from S3, configures merge settings using finance_id
    as the merge key, and loads the data into the agrolift_schema in Snowflake.

    Returns:
        None
    """
    pipeline = dlt.pipeline(
        pipeline_name="financial",
        destination='snowflake',
        dataset_name="agrolift_schema",
    )
   
    financial_files = readers(bucket_url=TESTS_BUCKET_URL, file_glob="mock_data/dim_financial/*.parquet").read_parquet()
    financial_files.apply_hints(write_disposition="merge", merge_key="finance_id")

    load_info = pipeline.run(financial_files.with_name("DIM_FINANCIALS"),)
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    farm_merge()
    farmers_merge()
    financial_merge()
