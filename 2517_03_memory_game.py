memory = input().split(" ")
command = input()
count = 1

while command != "end":
    ind1 = int(command.split(" ")[0])
    ind2 = int(command.split(" ")[1])
    if ind1 < 0 or ind2 < 0 or ind1 >= len(memory) or ind2 >= len(memory) or ind1 == ind2:
        new_el = '-' + str(count) + 'a'
        index = int(len(memory) / 2)
        memory.insert(index,new_el)
        memory.insert(index,new_el)
        print(f'Invalid input! Adding additional elements to the board')
    else:
        if memory[ind1] == memory[ind2]:
            print(f'Congrats! You have found matching elements - {memory[ind2]}!')
            rem_el = memory[ind1]
            memory.remove(rem_el)
            memory.remove(rem_el)
        else:
            print('Try again!')
    if len(memory) == 0:
        print(f'You have won in {count} turns!')
        break

    count += 1
    command = input()

if len(memory) > 0:
    print(f'Sorry you lose :(')
    print(' '.join(memory))
