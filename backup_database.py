import sqlite3

source = sqlite3.connect("sales_data.db")
backup = sqlite3.connect("sales_data_backup.db")

source.backup(backup)

backup.close()
source.close()

print("Database backup created successfully!")

