import sqlite3

DB_NAME = "sales_data.db"


def create_database():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_number TEXT,
            sale_date TEXT,
            transaction_time TEXT,
            sale_amount REAL,
            tax_amount REAL,
            discount_amount REAL,
            round_off REAL,
            net_sale REAL,
            payment_mode TEXT,
            order_type TEXT,
            transaction_status TEXT
        )
    """)

    conn.commit()
    conn.close()

    print("Database table is ready!")


def insert_sales_data(records):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE UNIQUE INDEX IF NOT EXISTS
    unique_sale_record
    ON sales_data (receipt_number, sale_date)
""")

    inserted_count = 0

    for record in records:

        cursor.execute("""
          INSERT OR IGNORE INTO sales_data (
                receipt_number,
                sale_date,
                transaction_time,
                sale_amount,
                tax_amount,
                discount_amount,
                round_off,
                net_sale,
                payment_mode,
                order_type,
                transaction_status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            record.get("Receipt number"),
            record.get("Receipt Date"),
            record.get("Transaction Time"),
            record.get("Invoice amount"),
            record.get("Tax amount"),
            record.get("Discount amount"),
            record.get("Round Off"),
            record.get("Net sale"),
            record.get("Payment Mode"),
            record.get("Order Type"),
            record.get("Transaction status")
        ))

        inserted_count += 1

    conn.commit()
    conn.close()

    print(f"Successfully inserted {inserted_count} sales records!")