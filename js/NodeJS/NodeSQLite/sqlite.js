const sqlite3 = require("sqlite3");
const db = new sqlite3.Database("../../../database/northwind.db");

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
readline.question(
  `Please select your choice:
1. List Finnish customers
2. List London employees
3. List Tofu sales.
Please enter your choice (1-3): `,
  (choice) => {
    console.log(`You selected choice ${choice}.`);
    readline.close();
    switch (choice) {
      case "1":
        listFinnishCustomers();
        break;
      case "2":
        listLondonCustomers();
        break;
      case "3":
        listTofuSales();
        break;
    }
  }
);

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
