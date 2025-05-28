# Data Ingestion Setup Guide

This guide explains how to set up and configure the data ingestion pipeline using DLT (Data Load Tool) with S3 and Snowflake.

## Prerequisites

- Python 3.11+
- Access to S3 bucket
- Snowflake account
- Filesystem access

## Installation Steps

1. **Create Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate
```

2. **Install Required Packages**
```bash
# Install DLT with required dependencies
pip install "dlt[s3,filesystem,snowflake]"

# Install PyArrow for Parquet support
pip install pyarrow
```

3. **Initialize DLT Project**
```bash
# Initialize DLT with filesystem and snowflake destinations
dlt init filesystem snowflake
```

## Configuration

1. **Configure `secrets.toml`**
   - Set up your credentials and configurations in `secrets.toml`
   - Include:
     - source and destination settings

2. **Configure the filesystem_pipeline Script**
   - Modify the Script to suit the you ingestion method
   (Note: method used in the script is merge)

3. **Run the script:**
```
python filesystem_pipeline.py
```

