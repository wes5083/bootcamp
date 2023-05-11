using Microsoft.AspNetCore.Mvc;
using System.Data.SQLite;
 

namespace OperateSQLite.Controllers;

[ApiController]
[Route("api/")]
 
public class OperateSQLiteController : ControllerBase
{


    [Route("GetCustomers")]
    public List<Customer> GetCustomers()
    {

        SQLiteConnection connection = new SQLiteConnection("Data Source=C:\\00_zyw\\500_Bootcamp\\bootcamp\\database\\northwind.db");
        connection.Open();

        string sql = "SELECT * FROM Customers";

        SQLiteCommand command = new SQLiteCommand(sql, connection);
        SQLiteDataReader reader = command.ExecuteReader();

        List<Customer> result = new List<Customer>();
        while (reader.Read())
        {
            Customer customer = new Customer();
            customer.CustomerID = reader["CustomerID"]?.ToString() ?? "";
            customer.CompanyName = reader["CompanyName"]?.ToString() ?? "";
            customer.ContactName = reader["ContactName"]?.ToString() ?? "";
            customer.ContactTitle = reader["ContactTitle"]?.ToString() ?? "";
            customer.Address = reader["Address"]?.ToString() ?? "";
            customer.City = reader["City"]?.ToString() ?? "";
            customer.Region = reader["Region"]?.ToString() ?? "";
            customer.PostalCode = reader["PostalCode"]?.ToString() ?? "";
            customer.Country = reader["Country"]?.ToString() ?? "";
            customer.Phone = reader["Phone"]?.ToString() ?? "";
            customer.Fax = reader["Fax"]?.ToString() ?? "";
            result.Add(customer);
        }

        reader.Close();
        connection.Close();
        return result;
    }


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
