import re
my_text = input()
expresion = r"([\||\#])(?P<food>[a-zA-Z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<cal>\d+)\1"
matches = re.finditer(expresion, my_text)

foods = dict()
total_cal = 0
count = 1
for match in matches:
    food = match.group("food")
    date = match.group("date")
    cal = int(match.group("cal"))
    foods[count] = list()
    foods[count].append(food)
    foods[count].append(date)
    foods[count].append(cal)
    total_cal += cal
    count += 1

print(f'You have food to last you for: {total_cal//2000} days!')

for key in foods.keys():
    print(f'Item: {foods[key][0]}, Best before: {foods[key][1]}, Nutrition: {foods[key][2]}')
    
