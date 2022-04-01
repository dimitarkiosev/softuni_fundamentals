my_key = input()

line = input()

while line != 'Generate':
    all_info = line.split('>>>')
    command = all_info[0]

    if command == 'Contains':
        substring = all_info[1]
        if substring in my_key:
            print(f'{my_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif command == 'Flip':
        command2 = all_info[1]
        start_index = int(all_info[2])
        final_index = int(all_info[3])
        before = my_key[:start_index]
        after = my_key[final_index:]
        new = my_key[start_index:final_index]
        if command2 == 'Upper':
            new = new.upper()
        elif command2 == 'Lower':
            new = new.lower()
        my_key = before + new + after
        print(my_key)

    elif command == 'Slice':
        start_index = int(all_info[1])
        final_index = int(all_info[2])
        before = my_key[:start_index]
        after = my_key[final_index:]
        my_key = before + after
        print(my_key)

    line = input()

print(f'Your activation key is: {my_key}')
