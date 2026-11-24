# PETPOOJA SALES SYNC - Fetch and Store Sales Data

## Project Overview

This project fetches sales data from the Petpooja API,
processes the JSON response, and stores the sales records
in a local SQLite database using Python.

## Technologies Used

- Python
- REST API
- SQLite
- Requests
- Python Dotenv

## Project Structure

machine-test-sales-data/
│
├── main.py
├── database.py
├── check_database.py
├── backup_database.py
├── remove_duplicates.py
├── sales_data.db
├── requirements.txt
├── .env
├── .gitignore
└── README.md

## Features

- Fetch sales data from Petpooja API.
- Process JSON response.
- Store sales data in SQLite.
- Handle API errors.
- Retry failed API requests.
- Prevent duplicate records.
- Verify stored database records.

## Database Fields

- id
- receipt_number
- sale_date
- transaction_time
- sale_amount
- tax_amount
- discount_amount
- round_off
- net_sale
- payment_mode
- order_type
- transaction_status

## Installation

1. Clone the repository.

2. Create virtual environment:

   python3 -m venv venv

3. Activate virtual environment:

   source venv/bin/activate

4. Install dependencies:

   pip install -r requirements.txt

5. Configure API credentials in .env.

6. Run the application:

   python main.py

## Database Verification

Run:

python check_database.py

## Output

Successfully fetched and stored 1287 sales records
in the SQLite database during testing.

## Security

API credentials are stored in environment variables.
The .env file is excluded from GitHub.



## Error Handling

- Handles API connection and HTTP errors.
- Handles request timeouts and invalid JSON.
- Implements 3 retry attempts for API failures.
- Handles SQLite database errors.
- Uses commit and rollback for database transactions.
- Prevents duplicate records using a unique index.
-