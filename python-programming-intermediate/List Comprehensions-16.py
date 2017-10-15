## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]


for i, item in enumerate(ships):
    print(item)
    print(cars[i])
    

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, item in enumerate(things):
    item.append(trees[i])
    

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [item*2 for item in apple_prices]
apple_prices_lowered = [item-100 for item in apple_prices]

## 5. Counting Female Names ##

name_counts = {}

for item in legislators:
    name = item[1]
    gender = item[3]
    year = item[7]
    if gender =="F" and year >1940:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
  

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []

checks = [item is not None and item >30 for item in values]

## 8. Highest Female Name Count ##

max_value = None

for item in name_counts:
    count = name_counts[item]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}

for item_key, item_value in plant_types.items():
    print(item_key)
    print(item_value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for item_key, item_value in name_counts.items():
    if item_value == 2:
        top_female_names.append(item_key)
print(top_female_names)
    

## 11. Finding the Most Common Male Names ##

top_male_names = []

male_name_counts = {}

for item in legislators:
    gender = item[3]
    year = item[7]
    name = item[1]
    if gender == "M" and year > 1940:
        if name in male_name_counts:
            male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1

max_value = None
for item_key, item_value in male_name_counts.items():
    if max_value is None or item_value > max_value:
        max_value = item_value
highest_male_count = max_value

print(highest_male_count)
        
for item_key, item_value in male_name_counts.items():
    if item_value == highest_male_count:
        top_male_names.append(item_key)
        
print(top_male_names)
        
        
     