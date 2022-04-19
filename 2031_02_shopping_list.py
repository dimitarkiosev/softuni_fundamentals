shoping_list = input().split("!")
command_line = input()

while command_line != 'Go Shopping!':
    command = command_line.split(" ")[0]
    item = command_line.split(" ")[1]
    if command == 'Urgent':
        if item not in shoping_list:
            shoping_list.insert(0,item)
    elif command == 'Unnecessary':
        if item in shoping_list:
            shoping_list.remove(item)
    elif command == 'Rearrange':
        if item in shoping_list:
            shoping_list.remove(item)
            shoping_list.append(item)
    elif command == 'Correct':
        if item in shoping_list:
            new_item = command_line.split(" ")[2]
            ind1 = shoping_list.index(item)
            shoping_list.remove(item)
            shoping_list.insert(ind1, new_item)

    command_line = input()

print(", ".join(shoping_list))
