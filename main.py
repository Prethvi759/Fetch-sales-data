import os
import requests
from dotenv import load_dotenv
from database import create_database, insert_sales_data


# Load environment variables
load_dotenv()

# Read API details from .env
API_URL = os.getenv("API_URL")

params = {
    "app_key": os.getenv("APP_KEY"),
    "app_secret": os.getenv("APP_SECRET"),
    "access_token": os.getenv("ACCESS_TOKEN"),
    "restID": os.getenv("REST_ID"),
    "from_date": os.getenv("FROM_DATE"),
    "to_date": os.getenv("TO_DATE")
}


import time

def fetch_sales_data():

    max_retries = 3

    for attempt in range(1, max_retries + 1):

        try:
            print(f"Connecting to API... Attempt {attempt}")

            response = requests.get(
                API_URL,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            sales_data = response.json()

            if not isinstance(sales_data, dict):
                raise ValueError("Unexpected API response format")

            if "Records" not in sales_data:
                raise ValueError("Records field missing from API response")

            print("API connection successful!")

            return sales_data

        except requests.exceptions.RequestException as error:

            print("API error:", error)

            if attempt < max_retries:
                print("Retrying in 3 seconds...")
                time.sleep(3)

        except ValueError as error:

            print("Data error:", error)
            break

    print("API request failed after retries.")

    return None
if __name__ == "__main__":

    print("Starting sales data application...")

    create_database()

    sales_data = fetch_sales_data()

    if sales_data and "Records" in sales_data:

        records = sales_data["Records"]

        print("Total records received:", len(records))

        insert_sales_data(records)

    else:
        print("No sales records found!")