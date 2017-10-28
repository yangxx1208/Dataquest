## 1. Introduction ##

select * from recent_grads limit 5

## 2. Calculating Group-Level Summary Statistics ##

select Major_category, AVG(ShareWomen) from recent_grads group by Major_category 

## 3. Practice: Using GROUP BY ##

select Major_category, AVG(Employed)/AVG(Total) share_employed from recent_grads group by Major_category

## 4. Querying Virtual Columns With the HAVING Statement ##

SELECT Major_category, AVG(Low_wage_jobs) / AVG(Total) AS share_low_wage FROM recent_grads GROUP BY Major_category HAVING share_low_wage > .1;

## 5. Rounding Results With the ROUND() Function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 6. Nesting functions ##

SELECT Major_category, ROUND(AVG(College_jobs) / AVG(Total), 3) AS share_degree_jobs FROM recent_grads GROUP BY Major_category HAVING share_degree_jobs < .3;

## 7. Casting ##

SELECT Major_category, Cast(SUM(Women) as Float)/Cast(SUM(Total) as Float) SW FROM recent_grads GROUP BY Major_category ORDER BY SW