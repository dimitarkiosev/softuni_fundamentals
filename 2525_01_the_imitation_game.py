code = input()
new_code = ''

while True:
    command = input().split("|")
    if command[0] == 'Decode':
        print(f'The decrypted message is: {code}')
        break
    elif command[0] == 'Move':
        index = int(command[1])
        movement = code[:index]
        static = code[index:]
        code = static + movement
        
    elif command[0] == 'Insert':
        index = int(command[1])
        new_text = command[2]
        before = code[:index]
        after = code[index:]
        
        code = before + new_text + after
        
    elif command[0] == 'ChangeAll':
        cur_str = command[1]
        new_str = command[2]
        
        code = code.replace(cur_str, new_str)
