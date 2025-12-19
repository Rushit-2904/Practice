select * from walmart; 

select branch, city, unit_price
from walmart
where city like 's%e' and 
unit_price between 25 and 75
order by city desc;

select * from walmart where quarter is null;

select branch, city, unit_price, payment_method
from walmart
where city not like '%s%' and 
unit_price not between 25 and 75 and 
payment_method not in ('Ewallet', 'Cash')
order by city asc, unit_price desc;
-- fetch first 5 rows only; ORACLE DB

select city as shehar, unit_price as daam
from walmart w;

select distinct category from walmart;

SELECT DISTINCT
    city, category
FROM
    walmart
ORDER BY city ASC;

