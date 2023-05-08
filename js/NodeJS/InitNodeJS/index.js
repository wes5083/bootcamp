console.log("Hello world");

var fs = require("fs");
var file = "./northwind.db";
var exists = fs.existsSync(file);
var sqlite3 = require("sqlite3").verbose();
var db = new sqlite3.Database(file);

/*

//add
var sqlAdd = db.prepare("insert into 表名 values (内容，跟mysql一样)");
sqlAdd.run();
//delete
var sqlDelete = db.prepare("delete from 表名 where id = 1");
sqlDelete.run();
//update
var sqlUpdate = db.prepare("update 表名 set name = winston where id = 1");
sqlUpdate.run();
// query all
db.all("select * from 表名", function (err, row) {
  console.log(JSON.stringify(row));
});
//query one
db.each("select * from 表名", function (err, row) {
  console.log(row);
});

*/

db.all("select * from customers where Country='Finland'", function (err, row) {
  console.log("----------------Reads all Finnish customers-------------------");
  console.log(row);
  console.log("----------------Reads all Finnish customers-------------------");
});

db.all("select * from Employees where city='London'", function (err, row) {
  console.log("-----------------All employees from London------------------");
  console.log(row);
  console.log("-----------------All employees from London------------------");
});

db.each(
  "select sum(detail.UnitPrice * detail.Quantity *(1 - detail.Discount) ) from 'Order Details' as detail left join Products as product on detail.ProductID=product.ProductID  where product.ProductName='Tofu'",
  function (err, row) {
    console.log("-----------------The amount of Tofu sales------------------");
    console.log(row);
    console.log("-----------------The amount of Tofu sales------------------");
  }
);
