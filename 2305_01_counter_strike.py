energy = int(input())
distance = input()
count = 0

while distance != 'End of battle':
    if int(distance) > energy:
        print(f'Not enough energy! Game ends with {count} won battles and {energy} energy')
        break
    else:
        count += 1
        energy -= int(distance)
        if count % 3 == 0:
            energy += count
    distance = input()

if distance == 'End of battle':
    print(f'Won battles: {count}. Energy left: {energy}')
