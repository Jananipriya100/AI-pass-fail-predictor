import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Janupriya1820",  # replace with your actual MySQL password
        database="ai_microservice"
    )

    if connection.is_connected():
        print("✅ MySQL Connected Successfully")

except Exception as e:
    print("❌ Error:", e)