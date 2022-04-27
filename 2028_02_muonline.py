rooms = input().split("|")
health = 100
bitcoin = 0

for each in rooms:
    action = each.split(" ")[0]
    item = int(each.split(" ")[1])
    if action == 'potion':
        if health + item > 100:
            item = 100 - health
        health += item
        print(f'You healed for {item} hp.')
        print(f'Current health: {health} hp.')
    elif action == 'chest':
        bitcoin += item
        print(f'You found {item} bitcoins.')
    else:
        health -= item
        if health > 0:
            print(f'You slayed {action}.')
        else:
            print(f'You died! Killed by {action}.')
            print(f'Best room: {rooms.index(each) + 1}')
            break

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoin}")
    print(f"Health: {health}")
