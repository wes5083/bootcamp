using Microsoft.AspNetCore.Mvc;
using System.Data.SQLite;

namespace OperateSQLite.Controllers;

[ApiController]
[Route("api/")]
public class OperateSQLiteController : ControllerBase
{

    [Route("GetFinnishCustomers")]
    public List<string> GetFinnishCustomers()
    {

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


    [Route("AddFinnishCustomers")]
    public string AddFinnishCustomers()
    {

        SQLiteConnection connection = new SQLiteConnection("Data Source=C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db");
        connection.Open();

        string sql = "insert into " +
        "Customers('CustomerID','CompanyName','ContactName','ContactTitle','Address','City','Region','PostalCode','Country','Phone','Fax')" +
        "values" +
        "('ZYW_ID', 'ZYW', 'zyw_contractname', 'zyw_contracttitle', 'Espoo 001', 'Espoo', 'Espoo', 40012, 'Finland', '90-2248858', '90-224 8858')";

        SQLiteCommand command = new SQLiteCommand(sql, connection);
        command.ExecuteNonQuery();
        connection.Close();
        return "success";
    }

}
