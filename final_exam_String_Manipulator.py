mystring = input()
new_string = ''
line = input()

while line != 'End':
    command = line.split(' ')[0]
    if command == 'Translate':
        my_char = line.split(' ')[1]
        new_char = line.split(' ')[2]
        new_string = mystring.replace(my_char, new_char)
        print(new_string)

    elif command == 'Includes':
        my_char = line.split(' ')[1]
        if my_char in mystring:
            print(f'True')
        else:
            print(f'False')

    elif command == 'Start':
        my_char = line.split(' ')[1]
        if mystring[:len(my_char)] == my_char:
            print(f'True')
        else:
            print(f'False')

    elif command == 'Lowercase':
        new_string = mystring.lower()
        print(new_string)

    elif command == 'FindIndex':
        my_char = line.split(' ')[1]
        my_index = mystring.rindex(my_char)
        print(my_index)

    elif command == 'Remove':
        startIndex = int(line.split(' ')[1])
        count = int(line.split(' ')[2])
        nextIndex = startIndex + count
        new_string = mystring[:startIndex] + mystring[nextIndex:]
        print(new_string)

    mystring = new_string
    line = input()
