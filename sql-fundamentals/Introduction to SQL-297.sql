## 2. Previewing A Table Using SELECT ##

select * from recent_grads limit 10;

## 3. Filtering Rows Using WHERE ##

select Major, ShareWomen from recent_grads where ShareWomen < 0.5

## 4. Expressing Multiple Filter Criteria Using AND ##

SELECT Major, Major_category, Median, ShareWomen FROM recent_grads WHERE ShareWomen > 0.5 AND Median > 50000

## 5. Returning One of Several Conditions With OR ##

select Major, Median, Unemployed from recent_grads where Median >= 10000 or Unemployed <= 1000 limit 20


## 6. Grouping Operators With Parentheses ##

SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM recent_grads
WHERE (Major_category = 'Engineering') AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051);

## 7. Ordering Results Using ORDER BY ##

select major , sharewomen, unemployment_rate from recent_grads where sharewomen > 0.3 and unemployment_rate < 0.1 order by shareWomen desc

## 8. Practice Writing A Query ##

select major_category , major , unemployment_rate from recent_grads where major_category = 'Engineering' or major_category = 'Physical Sciences' order by unemployment_rate asc