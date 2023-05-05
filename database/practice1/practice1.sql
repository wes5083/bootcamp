
-- part1

select * from customers where Country='Finland';


select ord.* from Orders as  ord left join customers as customer on ord.CustomerID=customer.CustomerID  
where customer.CompanyName='Que Delícia';

select * from Employees where city='London';

-- part2

select count(1) from customers;

select sum(detail.UnitPrice * detail.Quantity - detail.Discount) 
    from 'Order Details' as detail left join Products as product on detail.ProductID=product.ProductID 
    where product.ProductName='Tofu';