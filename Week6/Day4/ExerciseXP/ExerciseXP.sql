-- select first_name as "FirstName" , last_name as "LastName" from employees
-- select * from employees

-- select department_id from employees

-- select * from employees order by first_name desc


--  select first_name,last_name,salary,salary * 0.85 as PF from employees

-- select * from employees

-- select employee_id,first_name,last_name,salary from employees order by salary asc 


-- SELECT SUM (DISTINCT  salary)
-- FROM employees;

-- SELECT MAX (salary)
-- FROM employees;

-- SELECT MIN (salary)
-- FROM employees;

-- SELECT AVG (salary)
-- FROM employees;

-- SELECT COUNT (*)
-- FROM employees;

-- SELECT UPPER(first_name) from employees 

-- SELECT LEFT(first_name,3) from employees;

-- select concat(first_name,' ',last_name) as full_name from employees;

-- SELECT concat(first_name,' ',last_name) as full_name LENGTH(full_name) from employees;

-- SELECT LENGTH(concat(first_name,' ',last_name)) AS full_name from employees;

-- select first_name from employees where first_name like '%[0-9]%';

-- select * from employees limit 10;

-- select first_name,last_name,salary from employees where salary between 10000 and 15000;

-- select * from employees
-- select first_name ,last_name,hire_date from employees where hire_date>'1987-01-01' and hire_date <'1987-12-31'

-- select first_name from employees where first_name like '%c%' or first_name like'%e' 

-- select * from employees

-- select last_name,job_title,salary
-- from employees,jobs where jobs.job_id = employees.job_id
-- and job_title='Programmer' or job_title='Shipping Clerk'
-- and salary =4500 or salary = 10000 or salary = 15000;

-- select last_name from employees where LENGTH(last_name) = 6

-- select last_name from employees where left(last_name,3) like '%e'

-- select job_title as "Job available" from jobs,employees where jobs.job_id = employees.job_id

select * from employees where last_name = 'JONES' or last_name = 'BLAKE' or last_name = 'SCOTT'
or last_name = 'King' or last_name = 'FORD'



