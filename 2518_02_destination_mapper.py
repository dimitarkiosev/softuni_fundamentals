import re
my_text = input()
expresion = r"(\=|\/)(?P<name>[A-Z][a-zA-Z]{2}[a-zA-Z]*)\1"
matches = re.finditer(expresion, my_text)

travel = list()
travel_points = 0

for match in matches:
    name = match.group("name")
    travel_points += len(name)
    travel.append(name)

print(f'Destinations: {", ".join(travel)}')
print(f'Travel Points: {travel_points}')
