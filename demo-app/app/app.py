from flask import Flask, request, jsonify
import psycopg2, os

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST")
    )

@app.route('/write', methods=['POST'])
def write():
    data = request.json.get("data")
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS messages (id SERIAL PRIMARY KEY, content TEXT);")
    cur.execute("INSERT INTO messages (content) VALUES (%s);", (data,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success", "data": data})

@app.route('/read', methods=['GET'])
def read():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT content FROM messages;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([r[0] for r in rows])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
