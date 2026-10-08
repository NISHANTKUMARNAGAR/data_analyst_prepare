"""import sqlite3
connection = sqlite3.connect("table1.db")
cursor = connection.cursor()
#for select -- fetchall()/fetchone()
#for insert,update,delete -- connection.commit()
cursor.execute("SELECT * FROM practice")
print(cursor.fetchall())"""

#sql retrieving data from table
#uses table practice from file table1.db
"""
SELECT * FROM practice;
SELECT name,city FROM practice;
SELECT DISTINCT city FROM practice;
SELECT name,city,commission FROM practice WHERE commission>0.13;
SELECT cust_name,city FROM practice WHERE city='London';
SELECT ord_no,purch_amt FROM practice WHERE purch_amt>1000;
SELECT ord_no,purch_amt,ord_date FROM practice WHERE purch_amt BETWEEN 100 AND 1000;
SELECT cust_name,city FROM practice WHERE city IN ('London','New York');
SELECT name,city FROM practice WHERE city<>'Paris';
SELECT name,city FROM practice WHERE city LIKE 'L%';
SELECT name,city,commission FROM practice WHERE commission BETWEEN 0.12 AND 0.15;
SELECT ord_no,purch_amt,ord_date FROM practice WHERE ord_date='2012-10-05';
SELECT cust_name,city,grade FROM practice WHERE grade>=200;
SELECT name,city,commission FROM practice WHERE commission<>0.13;
SELECT name,city,commission FROM practice WHERE commission>0.12 AND city='Paris';
SELECT name,city,commission FROM practice WHERE city IN ('Paris','Rome') AND commission>0.12;
SELECT name,city,commission FROM practice WHERE city NOT IN ('Paris','London');
SELECT name,city FROM practice WHERE city LIKE '%o%';
SELECT name,city FROM practice WHERE city LIKE '%n';
SELECT name,city FROM practice WHERE city LIKE '%i%';
SELECT name,city FROM practice WHERE city LIKE '%i__'; #last 3rd is 'i' then only 2 letters
SELECT name,city,commission FROM practice WHERE commission>0.13 OR city='London';
SELECT name,city,commission FROM practice WHERE commission>0.12 AND commission<0.15;
SELECT name,city,commission FROM practice WHERE commission IN (0.13,0.15);
SELECT ord_no,purch_amt,ord_date FROM practice WHERE purch_amt<500;
SELECT cust_name,city,grade FROM practice WHERE grade BETWEEN 100 AND 300;
SELECT pro_name,pro_price FROM practice WHERE pro_price>500;
SELECT pro_name,pro_price FROM practice WHERE pro_price BETWEEN 500 AND 3000;
SELECT DISTINCT salesman_id FROM practice;
SELECT cust_name,grade FROM practice;
SELECT ord_no,purch_amt FROM practice WHERE purch_amt<>2480.40;
SELECT * FROM practice LIMIT 0,5;
SELECT COUNT(pro_id) FROM practice;
SELECT MAX(pro_price) FROM practice;
SELECT MIN(pro_price) FROM practice;
SELECT AVG(pro_price) FROM practice
SELECT COUNT(customer_id) FROM (SELECT customer_id FROM practice GROUP BY customer_id HAVING COUNT(grade)>=1)
SELECT city,MAX(grade) FROM practice GROUP BY city
SELECT customer_id,ord_date,MAX(purch_amt) FROM practice GROUP BY customer_id,ord_date
SELECT salesman_id,purch_amt FROM practice WHERE ord_date='2012-08-17' GROUP BY salesman_id 
SELECT customer_id,MAX(purch_amt) FROM practice WHERE customer_id BETWEEN 3002 AND 3007 GROUP BY customer_id HAVING MAX(purch_amt)>1000
SELECT city,COUNT(salesman_id) FROM practice WHERE source_type='salesman' GROUP BY city
SELECT emp_dept,COUNT(emp_idno) FROM practice WHERE source_type='emp_details' GROUP BY emp_dept
"""

#uses table 2 specifically for orerby,groupby,,agg func
#sorting and filtering hr
"""
SELECT first_name ||' '|| last_name AS full_name,salary FROM employees WHERE salary<6000
SELECT first_name||' '||last_name as full_name FROM employees WHERE first_name NOT LIKE '%M%' ORDER BY department_id
SELECT * FROM employees WHERE (salary BETWEEN 8000 AND 12000 AND commission_pct IS NOT NULL) OR hire_date>'2003-06-05' AND department_id NOT IN (40,120,70)) #considering both date col and given date in iso format i.e. yyyy-mm-dd
SELECT first_name||' '||last_name AS full_name,salary FROM employees WHERE salary NOT BETWEEN 7000 AND 15000 ORDER BY first_name||' '||last_name ASC
SELECT first_name||' '||last_name AS full_name,employee_id,hire_date FROM employees WHERE hire_date BETWEEN '2007-11-05' AND '2009-07-05'
SELECT * FROM employees WHERE (first_name LIKE '%D%') OR (first_name LIKE '%S%') OR (first_name LIKE '%N%')
SELECT first_name||' '||last_name,commission_pct,email,REPLACE(phone_number,'.','-') AS phone_number,salary FROM employees WHERE salary>11000 AND phone_number LIKE '______3%' ORDER BY first_name DESC
SELECT employee_id FROM job_history GROUP BY employee_id HAVING COUNT(*)=2
SELECT employee_id FROM job_history WHERE employee_id LIKE '2%' GROUP BY employee_id HAVING COUNT(*)=2
SELECT job_id,COUNT(*) AS count,SUM(salary) AS sum,MAX(salary)-MIN(salary) AS salary_difference FROM employees GROUP BY job_id
SELECT job_id FROM job_history WHERE start_date-end_date>300 GROUP BY job_id HAVING COUNT(*)>=2
SELECT country_id,COUNT(city) FROM locations GROUP BY country_id
SELECT manager_id,COUNT(employee_id) FROM employees GROUP BY manager_id
SELECT department_id,AVG(salary) FROM employees WHERE commission_pct IS NOT NULL GROUP BY department_id
SELECT DISTINCT department_id FROM employees GROUP BY department_id, manager_id HAVING COUNT(employee_id) >= 4;
SELECT department_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY department_id HAVING COUNT(employee_id)>10
SELECT job_id,AVG(salary) FROM employees GROUP BY job_id HAVING AVG(salary)>8000
#now below 2 query have problem when end_date or * would mean you want to select 1 value for whole group which is 
#impossible to select as a single employee_id can have multiple end_date because of multiple jobs and same multiple col
#values for 2nd query when we write * so which should it select, thats why its better to have only gtoupby col and a agg func
#after select ,the only case it might work is when you write HAVING COUNT(*)=1 as then sql can select values of that record only
SELECT employee_id,end_date FROM job_history GROUP BY employee_id HAVING COUNT(*)>1
SELECT * FROM jobs GROUP BY job_id HAVING COUNT(*)=1 ORDER BY job_title DESC
"""

#sql joins and sql join in hr database
#table3
"""
SELECT s.name,c.cust_name,c.city FROM salesman s INNER JOIN customer c on s.city=c.city
SELECT o.ord_no,o.purch_amt,c.cust_name,c.city FROM customer c INNER JOIN (SELECT * FROM orders WHERE purch_amt BETWEEN 500 AND 2000) AS o on c.customer_id=o.customer_id
SELECT c.cust_name,c.city,s.salesman_id,s.commission FROM customer c INNER JOIN salesman s on c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,c.salesman_id,s.commission FROM customer c INNER JOIN (SELECT * FROM salesman WHERE commission>0.12) AS s on c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,s.salesman_id,s.city,s.commission FROM customer c INNER JOIN (SELECT * FROM salesman WHERE commission>0.12) AS s on c.salesman_id=s.salesman_id WHERE c.city<>s.city
SELECT o.ord_no,o.ord_date,o.purch_amt,c.cust_name as 'Customer',c.grade,s.name as 'Salesman',s.commission FROM orders o INNER JOIN customer c on o.customer_id=c.customer_id INNER JOIN salesman s on o.salesman_id=s.salesman_id
SELECT * FROM orders NATURAL JOIN customer NATURAL JOIN salesman
SELECT c.cust_name,c.city,c.grade,s.name,s.city FROM (SELECT * FROM customer WHERE grade<300) AS c INNER JOIN salesman s ON c.salesman_id=s.salesman_id ORDER BY c.customer_id ASC
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM customer c LEFT JOIN orders o ON c.customer_id=o.customer_id ORDER BY o.ord_date ASC
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt,s.name,s.commission FROM customer c LEFT JOIN orders o ON c.customer_id=o.customer_id LEFT JOIN salesman s ON c.salesman_id=s.salesman_id
SELECT * FROM salesman s LEFT JOIN customer c ON c.salesman_id = s.salesman_id ORDER BY s.name;
SELECT c.cust_name,c.city,c.grade,o.ord_no,o.ord_date,o.purch_amt FROM customer c LEFT JOIN orders o on c.customer_id=o.customer_id FULL OUTER JOIN salesman s on s.salesman_id=c.salesman_id 
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c LEFT JOIN (SELECT * FROM orders WHERE purch_amt>=2000) AS o ON c.customer_id=o.customer_id FULL OUTER JOIN salesman s ON c.salesman_id=s.salesman_id
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM customer c RIGHT JOIN orders o ON c.customer_id=o.customer_id
SELECT c.cust_name,c.city,o.ord_no,o.ord_date,o.purch_amt FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c RIGHT JOIN orders o ON c.customer_id=o.customer_id
SELECT * FROM customer CROSS JOIN salesman
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) CROSS JOIN (SELECT * FROM salesman WHERE city IS NOT NULL)
SELECT * FROM (SELECT * FROM customer WHERE grade IS NOT NULL) AS c CROSS JOIN (SELECT * FROM salesman WHERE city IS NOT NULL) AS s WHERE s.city<>c.city
SELECT * FROM company_mast AS c CROSS JOIN item_mast AS i WHERE c.com_id=i.pro_com
SELECT i.pro_name,i.pro_price,c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com
SELECT AVG(i.pro_price),c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com GROUP BY c.com_name
SELECT AVG(i.pro_price),c.com_name FROM company_mast AS c INNER JOIN item_mast AS i WHERE c.com_id=i.pro_com GROUP BY c.com_name HAVING AVG(i.pro_price)>=350
#next two are 2 ways to same question
SELECT a.pro_name,b.mostexp,a.acomname FROM (SELECT c.com_name AS acomname,i.pro_name,i.pro_price AS acompprice FROM company_mast AS c INNER JOIN item_mast AS i ON c.com_id=i.pro_com) AS a INNER JOIN (SELECT MAX(i.pro_price) AS mostexp,c.com_name AS bcomname FROM company_mast AS c INNER JOIN item_mast AS i ON c.com_id=i.pro_com GROUP BY c.com_name) AS b on a.acompprice=b.mostexp AND a.acomname=b.bcomname
SELECT A.pro_name, A.pro_price, F.com_name FROM item_mast A INNER JOIN company_mast F ON A.pro_com = F.com_id AND A.pro_price = (SELECT MAX(A.pro_price) FROM item_mast A WHERE A.pro_com = F.com_id)
SELECT d.dpt_name FROM (SELECT emp_dept FROM emp_details GROUP BY emp_dept HAVING COUNT(*)>2) AS e INNER JOIN emp_department AS d on e.emp_dept=d.dpt_code
SELECT c.cust_name FROM customer c LEFT JOIN orders o ON c.customer_id = o.customer_id WHERE o.customer_id IS NULL;
SELECT d.department_name,e.first_name || ' ' || e.last_name AS full_name FROM departments d INNER JOIN employees e ON d.manager_id = e.employee_id;
#table 2 (self join)
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e JOIN employees m ON m.employee_id=e.manager_id                                     # employee - manager pair
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id                                # match + employee without manager
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e RIGHT JOIN employees m ON m.employee_id=e.manager_id                               # match + manager without employee
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e LEFT JOIN employees m ON m.employee_id=e.manager_id WHERE e.manager_id IS NULL     # employee without manager
SELECT e.first_name AS worker,m.first_name AS manager FROM employees e RIGHT JOIN employees m ON m.employee_id=e.manager_id WHERE m.employee_id IS NULL   # manager without employee
SELECT e.first_name,e.last_name,e.department_id FROM employees AS e INNER JOIN (SELECT * FROM employees WHERE last_name='Taylor') AS m on m.department_id=e.department_id
#non-equi/range join
#table 2's employee and a new table 
#job_grade
------------+-----------+ -----------
GRADE_LEVEL | LOWEST_SAL|HIGHEST_SAL 
------------+-----------+ -----------
A              1000        2999
B              3000        5999
C              6000        9999
D             10000       14999
E             15000       24999
F             25000       40000

SELECT e.first_name,e.last_name,e.salary,j.grade_level FROM employees e INNER JOIN job_grade j ON e.salary BETWEEN j.lowest_sal AND j.highest_sal
"""

#sql CASE,WHEN,THEN,ESLE,END,combining query results (union/union all etc)
"""
#CASE,WHEN,THEN,ESLE,END use table 2
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN 'high' WHEN salary BETWEEN 3000 AND 4999 THEN 'medium' ELSE 'low' END AS 'salary_category' FROM employees
SELECT first_name,last_name,department_id,CASE department_id WHEN 100 THEN 'management' WHEN 200 THEN 'technical' WHEN 300 THEN 'support' ELSE 'other' END AS 'department_type' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 'above average' WHEN salary BETWEEN 3000 AND 5000 THEN 'average' ELSE 'below average' END AS 'salary_status' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 0.2*salary WHEN salary BETWEEN 3000 AND 5000 THEN 0.1*salary ELSE 0.05*salary END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 OR department_id=100 THEN 'high priority' ELSE 'normal priority' END AS 'salary_priority' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary IS NOT NULL THEN 'salary available' WHEN salary IS NULL THEN 'salary missing' END AS 'salary_info' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN 'high' WHEN salary<5000 THEN 'low' END AS 'salary_order' FROM employees ORDER BY salary_order ASC
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 AND department_id=100 THEN 0.2*salary WHEN salary>=5000 AND department_id<>100 THEN 0.1*salary ELSE 0 END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN CASE WHEN department_id=100 THEN "high_ management" ELSE "high_staff" END WHEN salary<5000 THEN 'low salary' END AS 'salary_label' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>5000 THEN 'high' WHEN salary BETWEEN 3000 AND 5000 THEN 'medium' WHEN salary<3000 THEN 'low'  END AS 'salary_category' FROM employees ORDER BY CASE WHEN salary_category='high' THEN 1 WHEN salary_category='medium' THEN 2 WHEN salary_category='low' THEN 3 END
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN ROUND(0.2*salary,2) WHEN salary BETWEEN 3000 AND 4999 THEN ROUND(0.1*salary,2) WHEN salary<3000 THEN ROUND(0.05*salary,2) END AS 'salary_bonus' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary IS NULL THEN 'not provided' ELSE salary END AS 'salary_display' FROM employees
SELECT first_name,last_name,salary,CASE WHEN salary>=5000 THEN CASE WHEN salary>=10000 THEN 'very high' ELSE 'high' END WHEN salary<5000 THEN CASE WHEN salary>=3000 THEN 'medium' ELSE 'low' END END AS salary_level FROM employees
SELECT SUM(CASE WHEN salary>=5000 THEN 1 ELSE 0 END) FROM employees
SELECT SUM(CASE WHEN salary>=5000 THEN 1 ELSE 0 END)  as high_salary_count,SUM(CASE WHEN salary<5000 THEN 1 ELSE 0 END) as low_salary_count FROM employees
#combining query results (union/union all etc) use table 3
SELECT salesman_id AS id,name,'salesman' AS label FROM salesman WHERE city='London' UNION SELECT customer_id,cust_name,'customer' FROM customer WHERE city='London'
SELECT customer_id,salesman_id FROM orders UNION SELECT customer_id,salesman_id FROM customer
SELECT salesman_id,city FROM customer UNION ALL SELECT salesman_id,city FROM salesman
SELECT salesman_id,city FROM salesman EXCEPT SELECT salesman_id,city FROM customer
SELECT city FROM salesman INTERSECT SELECT city FROM customer ORDER BY city
SELECT city FROM customer EXCEPT SELECT city FROM salesman UNION SELECT city FROM salesman EXCEPT SELECT city FROM customer
#combining above 2 topics using table 3
#https://www.w3resource.com/sql-exercises/union/sql-union.php
#q4--------------------------------------
SELECT s.name,o3.ord_no,o3.ord_date,o3.salesman_id,"highest" AS label FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MAX(purch_amt) AS mostexp,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostexp AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id 
UNION 
SELECT s.name,o3.ord_no,o3.ord_date,o3.salesman_id,"lowest" FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MIN(purch_amt) AS mostcheap,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostcheap AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id
#q5---------------------------------------
SELECT o3.salesman_id,s.name,o3.ord_no,"highest" AS label,o3.ord_date FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MAX(purch_amt) AS mostexp,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostexp AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id
UNION
SELECT o3.salesman_id,s.name,o3.ord_no,"lowest",o3.ord_date FROM salesman s INNER JOIN (SELECT o1.ord_no,o1.ord_date,o1.salesman_id FROM orders o1 INNER JOIN (SELECT MIN(purch_amt) AS mostcheap,ord_date FROM orders GROUP BY ord_date) AS o2  ON o1.purch_amt=o2.mostcheap AND o1.ord_date=o2.ord_date) AS o3 on o3.salesman_id=s.salesman_id 
ORDER BY ord_no
#q6---------------------------------------
SELECT s.salesman_id,s.name as salesman_name,CASE WHEN c.cust_name IS NOT NULL THEN cust_name WHEN c.cust_name IS NULL THEN 'NO MATCH' END AS customer_name,s.commission FROM salesman s LEFT JOIN customer c ON s.city=c.city ORDER BY salesman_name DESC
#q7---------------------------------------
SELECT DISTINCT s.salesman_id,s.name as salesman_name,s.city,CASE WHEN c.cust_name IS NOT NULL THEN 'MATCHED' WHEN c.cust_name IS NULL THEN 'NO MATCH' END AS city_match FROM salesman s LEFT JOIN customer c ON s.city=c.city
#q8--------------------------------------
SELECT customer_id,city,grade,"high" AS rating FROM customer WHERE grade>=300 UNION SELECT customer_id,city,grade,"low" AS rating FROM customer WHERE grade<300
#q9--------------------------------------
SELECT c.cust_name AS name,c.customer_id AS id FROM customer c INNER JOIN orders o ON c.customer_id=o.customer_id GROUP BY c.customer_id HAVING COUNT(*)>1 UNION SELECT s.name,s.salesman_id FROM salesman s INNER JOIN orders o ON s.salesman_id=o.salesman_id GROUP BY s.salesman_id HAVING COUNT(*)>1
"""

#sql fomatting output exercises
#table 3
"""
#SUBSTRING has 3 parameter item,start position,length in sql starts at index 1
SELECT salesman_id,name,city,commission*100||'%' FROM salesman
SELECT 'for '||ord_date||' there are '||COUNT(*)||' orders' FROM orders GROUP BY ord_date
SELECT name,city,SUBSTRING(name,1,3) AS name_start FROM salesman
SELECT UPPER(name),LOWER(city) FROM salesman
SELECT name,city,name||'-'||city AS salesman_info FROM salesman
SELECT name,city,SUBSTRING(name,-3) AS name_end FROM salesman
SELECT name,city,TRIM(name) AS clean_name FROM salesman
SELECT name,city,REPLACE(name,'a','@') AS formatted_name FROM salesman
SELECT name,city FROM salesman WHERE LENGTH(name)>5 
SELECT salesman_id,name,city,UPPER(name)||' | '||LOWER(city)||' | '||(commission*100)||'%' FROM salesman
"""

#null handling
#table 4
"""
SELECT customer_name,phone FROM customer_contact WHERE phone IS NULL
SELECT customer_name,COALESCE(credit_limit,0) FROM customer_contact
SELECT first_name,last_name,salary,bonus,salary+COALESCE(bonus,0) FROM employee_pay
SELECT order_id,product_name,quantity,unit_price,unit_price/NULLIF(quantity,0) AS price_per_unit  FROM sales_data
SELECT unit_price-unit_price*COALESCE(discount,0) AS price_per_unit FROM sales_data
SELECT COALESCE(phone,email,'No Contact Information') AS price_per_unit FROM customer_contact

"""

#sql date and time
#table 5
"""
SELECT first_name,hire_date FROM employees_dates WHERE hire_date BETWEEN '2022-01-01' AND '2024-12-31'
SELECT JULIANDAY(last_promotion)-JULIANDAY(hire_date) FROM employees_dates
SELECT * FROM orders_dates WHERE delivery_date BETWEEN order_date AND DATE(order_date,'+5 days')
SELECT STRFTIME('%Y',order_date),COUNT(*) FROM orders_dates GROUP BY STRFTIME('%Y',order_date)
SELECT STRFTIME('%Y-%m',order_date),AVG(amount) FROM orders_dates GROUP BY STRFTIME('%Y-%m',order_date)
SELECT * FROM orders_dates WHERE delivery_date>DATE(order_date,'+5 days')
SELECT * FROM 'employees_dates' WHERE contract_end<'2028-01-01'
"""

#sql subqueries
#table 2
"""
SELECT first_name,last_name FROM employees WHERE salary>(SELECT salary FROM employees WHERE employee_id=163)
SELECT first_name,last_name,department_id FROM employees WHERE salary IN (SELECT MIN(salary) FROM employees GROUP BY department_id)
SELECT * FROM employees WHERE salary>(SELECT AVG(salary) FROM employees)
SELECT first_name,last_name,department_id,salary FROM employees WHERE manager_id=(SELECT employee_id FROM employees WHERE first_name='Payam')
SELECT department_id,first_name,job_id,"Finance" AS department_name FROM employees WHERE department_id=(SELECT department_id FROM departments WHERE department_name='Finance')
SELECT * FROM employees WHERE salary BETWEEN (SELECT MIN(salary) FROM employees) AND 2500
SELECT * FROM employees WHERE department_id NOT IN (SELECT department_id FROM departments WHERE manager_id BETWEEN 100 AND 200)
SELECT * FROM employees WHERE salary=(SELECT MAX(salary) FROM employees WHERE salary<>(SELECT MAX(salary) FROM employees))
SELECT * FROM employees WHERE first_name<>'Clara' AND department_id=(SELECT department_id FROM employees WHERE first_name='Clara')
SELECT * FROM employees WHERE department_id IN (SELECT department_id FROM employees WHERE first_name LIKE '%T%')
SELECT * FROM employees WHERE salary>(SELECT AVG(salary) FROM employees) AND department_id IN  (SELECT department_id FROM employees WHERE first_name LIKE '%J%')
SELECT first_name,last_name,employee_id,job_id FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE location_id=(SELECT location_id FROM locations WHERE city='Toronto'))
SELECT first_name,last_name,employee_id,job_id FROM employees WHERE salary<ANY((SELECT salary FROM employees WHERE job_title='MK_MAN')) AND job_title<>'MK_MAN'
SELECT first_name,last_name,employee_id,job_id FROM employees WHERE salary>ALL((SELECT AVG(salary) FROM employees GROUP BY department_id))
SELECT d.department_id,(SELECT SUM(e.salary) FROM employees e WHERE e.department_id=d.department_id) AS SALARY_SUM_PER_DEPARTMENT FROM departments d WHERE d.manager_id<>0
SELECT employee_id,first_name||" "||last_name AS name,job_id,CASE WHEN job_id="ST_MAN" THEN "SALESMAN" WHEN job_id="IT_PROG" THEN "DEVELOPER" ELSE job_id END AS designation FROM employees
SELECT department_name FROM departments d WHERE EXISTS (SELECT 1 FROM employees e WHERE e.department_id=d.department_id)
SELECT last_name FROM employees WHERE salary>(SELECT AVG(salary) FROM employees) AND department_id=(SELECT department_id FROM departments WHERE department_name='IT')
#subquery in join was done earlier in joins learning exercise
"""

#sql cte
#table 3
"""
WITH customer_total AS (SELECT customer_id,SUM(purch_amt) AS total_order_amt FROM orders GROUP BY customer_id) SELECT customer_id,total_order_amt FROM customer_total
WITH customer_total AS (SELECT c.cust_name AS cust_name,o.purch_amt AS purch_amt FROM customer c INNER JOIN orders o  on c.customer_id=o.customer_id) SELECT cust_name,SUM(purch_amt) FROM customer_total GROUP BY cust_name HAVING SUM(purch_amt)>10000
WITH customer_total AS (SELECT c.cust_name AS cust_name,CASE WHEN o.purch_amt IS NOT NULL THEN o.purch_amt WHEN o.purch_amt IS NULL THEN 0 END AS purch_amt FROM customer c LEFT JOIN orders o  on c.customer_id=o.customer_id) SELECT cust_name,SUM(purch_amt) FROM customer_total GROUP BY cust_name 
WITH customer_total AS (SELECT c.cust_name AS cust_name,COALESCE(o.purch_amt,0) AS purch_amt FROM customer c LEFT JOIN orders o  on c.customer_id=o.customer_id) SELECT cust_name,SUM(purch_amt) FROM customer_total GROUP BY cust_name 
WITH salesman_total AS (SELECT salesman_id,SUM(purch_amt) AS total_order_amt FROM orders GROUP BY salesman_id) SELECT salesman_id,total_order_amt FROM salesman_total WHERE total_order_amt=(SELECT MAX(total_order_amt) FROM salesman_total)
WITH customer_details AS (SELECT c.cust_name AS c_name,o.customer_id AS c_id FROM customer c INNER JOIN orders o ON o.customer_id=c.customer_id),max_order_details AS (SELECT MAX(number_of_orders) AS max_orders FROM (SELECT COUNT(*)  AS number_of_orders FROM customer_details GROUP BY c_id)) SELECT c_name,c_id,COUNT(*) AS number_of_orders FROM customer_details GROUP BY c_id HAVING COUNT(*)=(SELECT max_orders FROM max_order_details)
WITH salesman_order_details AS (SELECT salesman_id,AVG(purch_amt) AS avg_purch FROM orders GROUP BY salesman_id) SELECT o.salesman_id,o.ord_no,o.purch_amt FROM orders o WHERE o.purch_amt>(SELECT avg_purch FROM salesman_order_details s WHERE s.salesman_id=o.salesman_id)
WITH customer_det AS (SELECT customer_id FROM orders GROUP BY customer_id HAVING SUM(purch_amt)>5000 AND COUNT(*)>=2) SELECT cust_name,customer_id FROM customer  WHERE customer_id IN (SELECT customer_id FROM customer_det)
WITH max_sale AS (SELECT salesman_id,MAX(purch_amt) AS max_purch FROM orders GROUP BY salesman_id),salesman_details AS (SELECT salesman_id,purch_amt,ord_no FROM orders) SELECT max_sale.salesman_id,max_sale.max_purch,salesman_details.ord_no FROM max_sale INNER JOIN salesman_details ON max_sale.salesman_id=salesman_details.salesman_id AND max_sale.max_purch=salesman_details.purch_amt
"""

#sql window functions
#table 2,table 3
"""SELECT employee_id,first_name,department_id,salary,AVG(salary) OVER (PARTITION BY department_id) AS avgsaldepwise FROM employees ORDER BY department_id
SELECT ord_no,salesman_id,ord_date,purch_amt,SUM(purch_amt) OVER (PARTITION BY salesman_id ORDER BY ord_date) AS curr_sum FROM orders
SELECT employee_id,first_name,department_id,salary,RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) FROM employees
SELECT ord_no,salesman_id,ord_date,purch_amt,LAG(purch_amt) OVER (PARTITION BY salesman_id ORDER BY ord_date) AS pre_amt FROM orders
SELECT employee_id,first_name,department_id,salary,salary-LAG(salary) OVER (PARTITION BY department_id ORDER BY salary) FROM employees
SELECT employee_id,first_name,department_id,salary,MAX(salary) OVER (PARTITION BY department_id) FROM employees
SELECT ord_no,salesman_id,ord_date,purch_amt,LEAD(purch_amt) OVER (PARTITION BY salesman_id ORDER BY ord_date) FROM orders
SELECT ord_no,salesman_id,purch_amt,purch_amt*100/SUM(purch_amt) OVER () FROM orders
SELECT employee_id,first_name,department_id,salary,salary*100/SUM(salary) OVER (PARTITION BY department_id) FROM employees
SELECT ord_no,salesman_id,ord_date,purch_amt,AVG(purch_amt) OVER (PARTITION BY salesman_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) FROM orders
SELECT employee_id,first_name,department_id,salary,COUNT(*) OVER (PARTITION BY department_id,salary) FROM employees
SELECT employee_id,first_name,department_id,salary,PERCENT_RANK() OVER (PARTITION BY department_id ORDER BY salary) FROM employees
SELECT employee_id,first_name,department_id,salary,MAX(salary) OVER w,MIN(salary) OVER w FROM employees WINDOW w AS (PARTITION BY department_id)
SELECT employee_id,first_name,department_id,salary,FIRST_VALUE(salary) OVER w,LAST_VALUE(salary) OVER w FROM employees WINDOW w AS (PARTITION BY department_id ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
WITH sal_data AS (SELECT *,RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS emp_rank FROM employees) SELECT * FROM sal_data WHERE emp_rank<3 #top 2 salary by department
SELECT employee_id,first_name,department_id,salary,NTILE(4) OVER (PARTITION BY department_id ORDER BY salary) FROM employees
SELECT employee_id, department_id, salary FROM employees ORDER BY AVG(salary) OVER(PARTITION BY department_id) DESC;
"""

#practical and data quality analysis
#table 6
"""SELECT customer_id FROM customer_data GROUP BY customer_id HAVING COUNT(*)>1 #duplicate customer_id
SELECT * FROM customer_data WHERE email IN (SELECT email FROM customer_data GROUP BY email HAVING COUNT(*)>1) #same email used by many people
SELECT * FROM customer_data WHERE email IS  NULL OR phone IS NULL OR city IS NULL OR signup_date IS NULL #atleast one is null btw email,phone,city,signup_date
SELECT * FROM customer_data WHERE city<>UPPER(SUBSTRING(city,1,1))||LOWER(SUBSTRING(city,2)) OR status<>UPPER(SUBSTRING(status,1,1))||LOWER(SUBSTRING(status,2)) #inconsistent capitalization
SELECT * FROM sales_data WHERE quantity<0 OR unit_price<0 OR discount NOT BETWEEN 0 AND 1 #removinh negative quantity or unit price or not required discount value"""
