my_num = int(input())
heroes = dict()

for _ in range(my_num):
    line = input()
    hero_name = line.split(" ")[0]
    HP = int(line.split(" ")[1])
    MP = int(line.split(" ")[2])
    if hero_name not in heroes.keys():
        heroes[hero_name] = [0, 0]
    heroes[hero_name][0] += HP
    heroes[hero_name][1] += MP

line = input()
while line != 'End':
    command = line.split(" - ")[0]
    hero = line.split(" - ")[1]
    if command == 'CastSpell':
        mp_need = int(line.split(" - ")[2])
        spell_name = line.split(" - ")[3]
        if heroes[hero][1] >= mp_need:
            heroes[hero][1] -= mp_need
            print(f'{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell_name}!')

    elif command == 'TakeDamage':
        damage = int(line.split(" - ")[2])
        attacker = line.split(" - ")[3]
        if damage >= heroes[hero][0]:
            heroes.pop(hero)
            print(f'{hero} has been killed by {attacker}!')
        else:
            heroes[hero][0] -= damage
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero][0]} HP left!')

    elif command == 'Recharge':
        amount = int(line.split(" - ")[2])
        if heroes[hero][1] + amount > 200:
            print(f'{hero} recharged for {200 - heroes[hero][1]} MP!')
            heroes[hero][1] = 200
        else:
            heroes[hero][1] += amount
            print(f'{hero} recharged for {amount} MP!')

    elif command == 'Heal':
        amount = int(line.split(" - ")[2])
        if heroes[hero][0] + amount > 100:
            print(f'{hero} healed for {100 - heroes[hero][0]} HP!')
            heroes[hero][0] = 100
        else:
            heroes[hero][0] += amount
            print(f'{hero} healed for {amount} HP!')

    line = input()

for each, values in heroes.items():
    print(f'{each}')
    print(f'  HP: {values[0]}')
    print(f'  MP: {values[1]}')
