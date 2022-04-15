targets = list(map(int, input().split(" ")))
command_l = input()

while command_l != 'End':
    command = command_l.split(" ")[0]
    c_index = int(command_l.split(" ")[1])
    c_value = int(command_l.split(" ")[2])
    if command == 'Shoot':
        if 0 <= c_index < len(targets):
            if c_value < targets[c_index]:
                targets[c_index] = targets[c_index] - c_value
            else:
                targets.pop(c_index)
    elif command == 'Add':
        if 0 <= c_index < len(targets):
            targets.insert(c_index,c_value)
        else:
            print(f'Invalid placement!')
    if command == 'Strike':
        if (c_index - c_value) < 0 or (c_index + c_value) >= len(targets):
            print(f'Strike missed!')
        else:
            for i in range(2*c_value + 1):
                targets.pop(c_index - c_value)
            # targets = targets[:c_index - c_value] + targets[c_index + c_value + 1:]
    command_l = input()

print("|".join([str(each) for each in targets]))
