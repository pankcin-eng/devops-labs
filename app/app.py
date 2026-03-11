from flask import Flask
import mysql.connector
import time
app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host='mysql-db', user='pank', password='devops_lab',
            database='devops_lab', port=3306)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logs")
        result = cursor.fetchall()
        conn.close()
        return f"Connected! Logs: {result}"
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    time.sleep(30)  # Wait for MySQL
    app.run(host='0.0.0.0', port=5000)
return f"Updated at {time.ctime()}! Logs: {result}"
return 'CI/CD LIVE! Deployed at Wed Mar 11 21:47:26 IST 2026'
# Auto-deploy test
return f'WEBHOOK TEST 'Wed Mar 11 21:57:17 IST 2026
return f'PUBLIC WEBHOOK {{time.ctime()}}! Logs: {{result}}'
return f'PUBLIC 38.254.189.62 LIVE {time.ctime()}! {{result}}'
return f'COMPLETE CI/CD {time.ctime()} LIVE! {{result}}'
