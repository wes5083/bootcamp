import sqlite3
import csv


def customers_finnish():
    con = sqlite3.connect("C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Customers WHERE Country = 'Finland'")
    data_list = cur.fetchall()
    cur.close()
    con.close()
    return data_list


def export_cvs():
    data_list = customers_finnish()
    print(data_list)
    columns = ['CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode',
               'Country',
               'Phone', 'Fax']
    with open("customers_finnish.csv", 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data_list)


customers_finnish()
export_cvs()
