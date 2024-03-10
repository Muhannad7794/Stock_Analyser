import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT")),
)

cursor = db.cursor()

# Create a new database only if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS stock_analyser")

print("Database checked/created successfully")

cursor.close()
db.close()
