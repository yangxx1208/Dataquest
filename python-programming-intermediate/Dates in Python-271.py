## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime(current_time)
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime as d

current_datetime = d.datetime.utcnow()

current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(2233,2,22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday- diff

## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime
mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date)

## 8. Reformatting Our Data ##

import datetime

for row in posts:
    row[2] = float(row[2])
    time = datetime.datetime.fromtimestamp(row[2])
    row[2] = time

## 9. Counting Posts from March ##

march_count = 0

for row in posts:
    if row[2].month ==3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
        
def find_month(a,data):
    count = 0
    for row in data:
        if row[2].month == a:
            count += 1
    return count

feb_count = find_month(2,posts)
aug_count = find_month(8,posts)            