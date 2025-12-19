select * from customers;

-- inner join (Uninon)
select a.customer_id,first_name,b.order_id,order_status,store_id
from customers a
inner join orders b on a.customer_id = b.customer_id
where order_status < 3 and store_id != 2
order by first_name desc;

--  left outer join (focuses on all rows in left table)
select a.staff_id,customer_id,order_status,a.store_id,b.first_name,phone,manager_id
from orders a
left outer join staffs b on a.staff_id = b.staff_id;
-- same way we have right outer(focuses on right table) full outer(focuses on both the tables)


-- left join (join the table with itself) and gives each staff's manager details

select a.staff_id,a.first_name,a.last_name,a.email,a.manager_id,b.first_name as manager ,b.last_name,b.email
from staffs a 
left join staffs b on a.manager_id = b.staff_id
order by staff_id;

-- cross join (basically gives each possibilities that can occur with two tables)
Select *
from stores a
cross join staffs b
order by a.store_id;

select * from order_items;
--  Aggregation and grouping

-- Average
select avg(list_price) 
from order_items
where discount > 0.1;

-- Sum
select sum(list_price)
from order_items
where product_id >10
order by order_id;

-- max and min

select max(list_price), min(list_price)
from order_items;

-- Count

select count(distinct product_id) -- gives the count of unique(because we used "distinct") product_id's in this table
from order_items;

select count(*)
from order_items; -- This gives the number of rows in order_items table

-- Group by (using aggregation fucntion on internal groups in a table)

select order_id, sum(quantity) total_quantity, sum(list_price) total_price, sum(discount)  total_discount, 
avg(list_price) avg_price, avg(discount) avg_discount
from order_items 
group by order_id
order by order_id;

-- Having (just Like WHERE, but for groups (not individual rows). Filters groups AFTER aggregation )

select order_id, sum(quantity) as total_quantity, sum(list_price) as total_price
from order_items
group by order_id
having total_price < 1000
order by order_id;

select * from order_items;

-- Sub query 

select count(*) from order_items 
where list_price> (select avg(list_price) from order_items);

-- Just like union and union all we can use "except" and this will negect the below query

select first_name from customers
where phone is not null
except
select first_name from customers
where state = 'CA';

-- Window functions
-- Rank, dense_rank, row_number
select product_id, product_name, brand_id, category_id, model_year, list_price, 
rank() over(order by list_price desc)as expesive_rank,
dense_rank() over(order by list_price desc)as expesive_dense_rank,
row_number() over(order by list_price desc)as expesive_row_number
from products;

-- using Partion by

select product_id, product_name, brand_id, category_id, model_year, list_price, 
rank() over(partition by model_year order by list_price desc)as expesive_rank
from products;

-- Top 3 for each year

select * from (select product_id, product_name, brand_id, category_id, model_year, list_price, 
rank() over(partition by model_year order by list_price desc)as expensive_rank
from products) as pop
where expensive_rank in (1,2,3)
order by model_year desc;

-- common table expression
















