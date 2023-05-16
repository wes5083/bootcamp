import sqlite3
import csv

db = "C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db"
csv_file = "customers_finnish.csv"
csv_title = ['CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode',
             'Country',
             'Phone', 'Fax']


def query(sql):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(sql)
    data_list = cur.fetchall()
    cur.close()
    con.close()
    return data_list


def customers_finnish():
    sql = "SELECT * FROM Customers WHERE Country = 'Finland'"
    return query(sql)


def export_cvs():
    sql = "SELECT * FROM Customers"
    csv_data = query(sql)
    with open(csv_file, 'w+', encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_title)
        writer.writerows(csv_data)


customers_finnish()
export_cvs()
