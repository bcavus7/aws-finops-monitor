# AWS FinOps Monitor

A Python tool that uses real AWS APIs to monitor cloud costs and budgets.

## Features
- Retrieve monthly AWS budget and actual spending
- Calculate remaining budget and usage percentage
- Display AWS Budget alert configurations
- Retrieve spending by AWS service using Cost Explorer

## Technologies
- Python
- Boto3 (AWS SDK)
- AWS Budgets API
- AWS Cost Explorer API
- Git

## Run
Requires Python, Boto3, and authenticated AWS credentials
with permission to read AWS Budgets and Cost Explorer.

Run:
python3 finops.py

## Current Limitations
- New AWS account has no spending history yet.
- Budget warning threshold is currently hardcoded.
- Cost Explorer API requests may incur charges.

## Cost Trend Analysis
Run `python cost_trends.py` to compare spending by
AWS service across the two most recent completed months.

The tool flags:
- Spending increases of 25% or more
- Newly appearing service costs

## Testing
Run `python -m pytest -v` to execute 8 automated tests.

## Data Limitations
The AWS account is newly created and has no historical
spending data. Cost comparison logic has been tested
with sample figures, not historical production bills.
