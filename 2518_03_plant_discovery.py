my_num = int(input())
plants = dict()

for _ in range(my_num):
    plant = input().split('<->')
    if plant[0] not in plants:
        plants[plant[0]] = [0,[]]
    plants[plant[0]][0] = plant[1]

line = input()

while line != 'Exhibition':
    command = line.split(': ')[0]
    cplant = line.split(': ')[1].split(' - ')[0]
    if cplant not in plants:
        print('error')

    elif command == 'Rate':
        new_rating = int(line.split(': ')[1].split(' - ')[1])
        plants[cplant][1].append(new_rating)

    elif command == 'Update':
        new_rarity = int(line.split(': ')[1].split(' - ')[1])
        plants[cplant][0] = new_rarity

    elif command == 'Reset':
        plants[cplant][1] = []

    line = input()

print(f'Plants for the exhibition:')
for (key,value) in plants.items():
    msum = sum(value[1])
    avg = 0
    if msum > 0:
        avg = msum / len(value[1])
    print(f'- {key}; Rarity: {value[0]}; Rating: {avg:.2f}')
