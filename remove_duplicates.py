import sqlite3

try:
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()

    # Count records before cleanup
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    before = cursor.fetchone()[0]

    print("Records before cleanup:", before)

    # Remove duplicate receipt/date combinations
    cursor.execute("""
        DELETE FROM sales_data
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM sales_data
            GROUP BY receipt_number, sale_date
        )
    """)

    deleted = cursor.rowcount

    # Prevent future duplicates
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS
        unique_sale_record
        ON sales_data (receipt_number, sale_date)
    """)

    conn.commit()

    # Count records after cleanup
    cursor.execute("SELECT COUNT(*) FROM sales_data")
    after = cursor.fetchone()[0]

    print("Duplicate records removed:", deleted)
    print("Records after cleanup:", after)
    print("Duplicate protection enabled!")

except sqlite3.Error as error:
    if conn:
        conn.rollback()
    print("Database error:", error)

finally:
    if conn:
        conn.close()