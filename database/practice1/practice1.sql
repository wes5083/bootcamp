
-- part1

-- All Finnish customers
select * from customers where Country='Finland';

-- All orders for the customer ”Que Delícia”
select ord.* from Orders as  ord left join customers as customer on ord.CustomerID=customer.CustomerID  
where customer.CompanyName='Que Delícia';

-- All employees from London
select * from Employees where city='London';

-- part2

-- How many customers does Northwind have?
select count(1) from customers;

-- How much tofu (in $) has Northwind sold?
select sum(detail.UnitPrice * detail.Quantity - detail.Discount) 
    from 'Order Details' as detail left join Products as product on detail.ProductID=product.ProductID 
    where product.ProductName='Tofu';