import logging

from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook

from scripts.config import (access_key, farmer_path, farm_path, bucket_name, secret_key,
                            snowflake_table, financial_path)

logging.basicConfig(format="%(asctime)s %(message)s")


def create_snowflake_table():
    """
    Executes a SQL script to create a table in Snowflake.

    This function reads an SQL file containing the create table statement
    and executes it using the SnowflakeHook to interact with Snowflake.

    Raises:
        Exception: If there is an error while reading the SQL file or
        executing the SQL command.
    """
    try:
        hook = SnowflakeHook(snowflake_conn_id="snow_flake")
        sql_file_path = "table_sql/create_table.sql"
        with open(sql_file_path, "r") as f:
            create_table_sql = f.read()

        hook.run(create_table_sql)
    except Exception as e:
        logging.info(f"error {e}")


def create_snowflake_stage():
    """
    Creates or replaces a Snowflake stage that points to an S3 bucket.

    This function constructs and executes a SQL query to create or replace a
    stage in Snowflake
    that links to a specified S3 bucket using provided AWS credentials.
    The stage will be configured to use the Parquet file format.

    Args:
        s3_bucket (str): The name of the S3 bucket.
        access_key (str): The AWS access key ID.
        secret_key (str): The AWS secret access key.

    Raises:
        Exception: If there is an error while executing the SQL query or
        setting up the stage.
    """
    hook = SnowflakeHook(snowflake_conn_id="snow_flake")
    try:

        sql_query = f"""
        CREATE OR REPLACE STAGE my_snowflake_stage
        URL = 's3://{bucket_name}/'
        CREDENTIALS = (AWS_KEY_ID = '{access_key}',
                    AWS_SECRET_KEY = '{secret_key}')
        FILE_FORMAT = (TYPE = PARQUET);
        """
        hook.run(sql_query)
    except Exception as e:
        logging.info(f"error {e}")


def load_farm_to_snowflake():
    """
    Loads a Parquet file from a Snowflake stage into a Snowflake table.

    This function constructs and executes a COPY INTO SQL command to load data
    from a Parquet file stored in a Snowflake stage into a specified Snowflake
    table.
    The file format is set to Parquet, and the matching of columns is
    case-insensitive.

    Args:
        parquet_path (str): The path to the Parquet file in the Snowflake
        stage.
        snowflake_table (str): The name of the Snowflake table into which the
        data will be loaded.

    Raises:
        Exception: If an error occurs during the loading process or while
        executing the SQL query.
    """
    try:
        hook = SnowflakeHook(snowflake_conn_id="snow_flake")

        sql_copy_into = f"""
        COPY INTO {snowflake_table}
        FROM @my_snowflake_stage/{farm_path}
        FILE_FORMAT = (TYPE = PARQUET)
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
        ON_ERROR = 'ABORT_STATEMENT';
        """

        hook.run(sql_copy_into)

    except Exception as e:
        logging.error(f"Failed to load Parquet to Snowflake:{e}",
                      exc_info=True)

def load_farmer_to_snowflake():
    """
    Loads a Parquet file from a Snowflake stage into a Snowflake table.

    This function constructs and executes a COPY INTO SQL command to load data
    from a Parquet file stored in a Snowflake stage into a specified Snowflake
    table.
    The file format is set to Parquet, and the matching of columns is
    case-insensitive.

    Args:
        parquet_path (str): The path to the Parquet file in the Snowflake
        stage.
        snowflake_table (str): The name of the Snowflake table into which the
        data will be loaded.

    Raises:
        Exception: If an error occurs during the loading process or while
        executing the SQL query.
    """
    try:
        hook = SnowflakeHook(snowflake_conn_id="snow_flake")

        sql_copy_into = f"""
        COPY INTO {snowflake_table}
        FROM @my_snowflake_stage/{farmer_path}
        FILE_FORMAT = (TYPE = PARQUET)
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
        ON_ERROR = 'ABORT_STATEMENT';
        """

        hook.run(sql_copy_into)

    except Exception as e:
        logging.error(f"Failed to load Parquet to Snowflake:{e}",
                      exc_info=True)
        
def load_financial_to_snowflake():
    """
    Loads a Parquet file from a Snowflake stage into a Snowflake table.

    This function constructs and executes a COPY INTO SQL command to load data
    from a Parquet file stored in a Snowflake stage into a specified Snowflake
    table.
    The file format is set to Parquet, and the matching of columns is
    case-insensitive.

    Args:
        parquet_path (str): The path to the Parquet file in the Snowflake
        stage.
        snowflake_table (str): The name of the Snowflake table into which the
        data will be loaded.

    Raises:
        Exception: If an error occurs during the loading process or while
        executing the SQL query.
    """
    try:
        hook = SnowflakeHook(snowflake_conn_id="snow_flake")

        sql_copy_into = f"""
        COPY INTO {snowflake_table}
        FROM @my_snowflake_stage/{financial_path}
        FILE_FORMAT = (TYPE = PARQUET)
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
        ON_ERROR = 'ABORT_STATEMENT';
        """

        hook.run(sql_copy_into)

    except Exception as e:
        logging.error(f"Failed to load Parquet to Snowflake:{e}",
                      exc_info=True)