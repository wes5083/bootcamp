const sqlite3 = require("sqlite3");
const db = new sqlite3.Database("../../../database/northwind.db");
listFinnishCustomers();
listLondonCustomers();
listTofuSales();

function listFinnishCustomers() {
  const sql = "SELECT * FROM Customers WHERE Country = 'Finland'";
  db.all(sql, (err, rows) => {
    rows.forEach((row) => {
      console.log(row.CompanyName);
    });
  });
}

function listLondonCustomers() {
  const sql = "select * from Employees where city='London'";
  db.all(sql, (err, rows) => {
    rows.forEach((row) => {
      console.log(row.FirstName + " " + row.LastName);
    });
  });
}
function listTofuSales() {
  const sql =
    "select sum(detail.UnitPrice * detail.Quantity *(1 - detail.Discount) ) as TofuSales" +
    " from 'Order Details' as detail left join Products as product on detail.ProductID=product.ProductID " +
    " where product.ProductName like'%Tofu%' ";
  db.all(sql, (err, rows) => {
    rows.forEach((row) => {
      console.log(row.TofuSales);
    });
  });
}
