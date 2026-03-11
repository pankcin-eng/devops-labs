import os
import mysql.connector
from datetime import datetime

db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'pank')
db_pass = os.getenv('DB_PASS', 'devops123')
db_name = os.getenv('DB_NAME', 'devops_lab')

try:
    conn = mysql.connector.connect(
        host=db_host, user=db_user, password=db_pass, database=db_name
    )
    cursor = conn.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255), timestamp DATETIME)")
    cursor.execute("INSERT INTO logs (message, timestamp) VALUES (%s, %s)", ("Hello from Docker Python app!", datetime.now()))
    conn.commit()
    
    cursor.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 3")
    results = cursor.fetchall()
    print("Recent logs from MySQL:")
    for row in results:
        print(row)
    
    cursor.close()
    conn.close()
    print("✅ MySQL connection successful!")
except Exception as e:
    print(f"❌ Error: {e}")
