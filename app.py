from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection details
db_config = {
    'user': 'root',
    'password': 'password',
    'host': 'db',
    'database': 'test_db'
}

@app.route('/')
def index():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        database = cursor.fetchone()[0]
        return jsonify({"database": database})
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

