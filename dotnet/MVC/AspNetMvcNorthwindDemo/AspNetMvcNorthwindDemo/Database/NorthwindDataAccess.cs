using System;
using System.Data.SQLite;

namespace AspNetMvcNorthwindDemo.Database
{
    public class NorthwindDataAccess
    {
        public List<string> GetFinnishCustomers() {
            SQLiteConnection connection = new SQLiteConnection("Data Source=C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db");
            connection.Open();

            string sql = "SELECT * FROM Customers WHERE Country = 'Finland'";

            SQLiteCommand command = new SQLiteCommand(sql, connection);
            SQLiteDataReader reader = command.ExecuteReader();

            List<string> result = new List<string>();
            while (reader.Read())
            {
                string companyName = reader["CompanyName"]?.ToString() ?? "";
                Console.WriteLine(companyName);
                result.Add(companyName);
            }

            reader.Close();
            connection.Close();
            return result;
        }
    }
}
