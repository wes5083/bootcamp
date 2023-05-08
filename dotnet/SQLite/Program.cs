using System;
using System.Data.SQLite;

namespace MyConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {

            SQLiteConnection connection = new SQLiteConnection("Data Source=C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db");
            connection.Open();

            string sql = "SELECT * FROM Customers WHERE Country = 'Finland'";

            SQLiteCommand command = new SQLiteCommand(sql, connection);
            SQLiteDataReader reader = command.ExecuteReader();

            while (reader.Read())
            {
                string companyName = reader["CompanyName"]?.ToString() ?? "";
                Console.WriteLine(companyName);
            }

            reader.Close();
            connection.Close();
        }
    }
}
