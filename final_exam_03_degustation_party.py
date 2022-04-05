line = input()
guests = dict()
unlike = 0
while line != 'Stop':
    command = line.split('-')[0]
    guest = line.split('-')[1]
    meal = line.split('-')[2]
    if command == 'Like':
        if guest not in guests.keys():
            guests[guest] = list()
        if meal not in guests[guest]:
            guests[guest].append(meal)
    if command == 'Dislike':
        if guest not in guests.keys():
            print(f'{guest} is not at the party.')
        else:
            if meal not in guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                unlike += 1
                guests[guest].remove(meal)
                print(f"{guest} doesn't like the {meal}.")

    line = input()

for key, value in guests.items():
    print(f"{key}: {', '.join(value)}")

print(f'Unliked meals: {unlike}')
