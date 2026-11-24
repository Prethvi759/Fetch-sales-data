import sqlite3

conn = None

try:
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()

    # Count records
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    total = cursor.fetchone()[0]

    print("Database connected successfully!")
    print("Total records:", total)

    # Display first 5 records
    cursor.execute("SELECT * FROM sales_data LIMIT 5")
    records = cursor.fetchall()

    print("\nFirst 5 records:")
    for record in records:
        print(record)

    # Check duplicates
    cursor.execute("""
        SELECT receipt_number, sale_date, COUNT(*)
        FROM sales_data
        GROUP BY receipt_number, sale_date
        HAVING COUNT(*) > 1
    """)

    duplicates = cursor.fetchall()

    print("\nDuplicate records found:", len(duplicates))

    for duplicate in duplicates:
        print(duplicate)

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed.")