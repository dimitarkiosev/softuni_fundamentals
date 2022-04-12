my_list = list(map(int,input().split(" ")))
command = input()

while command != 'end':
    new_command = command.split(" ")[0]

    if new_command == 'decrease':
        for x in range(len(my_list)):
            my_list[x] -= 1
    elif new_command == 'swap':
        ind1 = int(command.split(" ")[1])
        ind2 = int(command.split(" ")[2])
        my_list[ind1], my_list[ind2] = my_list[ind2], my_list[ind1]
    elif new_command == 'multiply':
        ind1 = int(command.split(" ")[1])
        ind2 = int(command.split(" ")[2])
        my_list[ind1] = my_list[ind1] * my_list[ind2]
    command = input()

new_list = [str(each) for each in my_list]
print(f'{", ".join(new_list)}')
