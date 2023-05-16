from flask import Flask, jsonify, request, json
import sqlite3

app = Flask(__name__)

db = "C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db"


@app.route("/customers", methods=['GET'])
def customers():
    con = sqlite3.connect(db)
    country = request.args.get("country", "")
    sql = "SELECT * FROM Customers "
    if country:
        sql = "SELECT * FROM Customers WHERE Country = '" + str(country) + "'"
    cur = con.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()
    cur.close()
    con.close()

    rows = []
    for row in data_list:
        row_dict = {
            'CustomerID': row[0],
            'CompanyName': row[1],
            'ContactName': row[2],
            'ContactTitle': row[3],
            'Address': row[4],
            'City': row[5],
            'Region': row[6],
            'PostalCode': row[7],
            'Phone': row[8],
            'Fax': row[9]
        }
        rows.append(row_dict)

    json_data = json.dumps(rows)

    return json_data


def json_print(json_object):
    return json.dumps(json_object)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='8001')
