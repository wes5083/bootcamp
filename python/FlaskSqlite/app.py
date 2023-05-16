from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = "C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db"


@app.route("/api/customers", methods=['GET'])
def customers():
    con = sqlite3.connect(db)
    sql = "SELECT * FROM Customers Where 1=1 "

    # params
    for key, value in request.args.items():
        sql += (" AND " + key + " = '" + value + "'")

    cur = con.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()
    cur.close()
    con.close()

    # column title
    column_names = [description[0] for description in cur.description]

    rows = []
    for row in data_list:
        rows.append(dict(zip(column_names, row)))
    return jsonify(rows)


if __name__ == '__main__':
    app.run()
