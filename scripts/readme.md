# Scripts Directory

This directory contains scripts for generating and managing agricultural data for the Agrolift project.

## Files

### mock_agriculture_data_generator2.py
- Main script for generating synthetic agriculture-related mock data
- Creates realistic sample data for testing and development purposes
- Generates data for farmers, farms, and financial histories

###
This `upload_to_s3` module provides functionality to save DataFrames as Parquet files to Amazon S3.

### util/config
- This `config.py` module contains configuration settings and data for the Agrolift agricultural data platform.

### util/session.py
- The `session.py` module contains functions to create authenticated AWS sessions using predefined credentials.

### pytest/test_mock_data.py
- The `test_mock_data.py` contains pytest test cases for validating the mock agricultural data generation functionality.

### ingestion/*
- Ingestion folder contain data ingestion script using dlthub from s3 to snowflake with the snowflake database, schema and tables manually created.