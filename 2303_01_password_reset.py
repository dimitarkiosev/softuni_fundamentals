my_pass = input()
line = input()

while line != 'Done':
    temp_string = ''
    command = line.split(" ")[0]
    if command == "TakeOdd":
        for i in range(len(my_pass)):
            if i % 2 == 1:
                temp_string += my_pass[i]
        print(temp_string)
        my_pass = temp_string

    elif command == "Cut":
        index = int(line.split(" ")[1])
        length = int(line.split(" ")[2])
        temp_string = my_pass[:index] + my_pass[index+length:]
        print(temp_string)
        my_pass = temp_string

    elif command == "Substitute":
        substring = line.split(" ")[1]
        substitute = line.split(" ")[2]
        if substring in my_pass:
            temp_string = my_pass.replace(substring,substitute)
            print(temp_string)
            my_pass = temp_string
        else:
            print(f'Nothing to replace!')

    line = input()

print(f'Your password is: {my_pass}')
