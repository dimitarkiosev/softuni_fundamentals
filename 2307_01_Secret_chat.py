message = input()
line = input()

while line != 'Reveal':
    command = line.split(':|:')[0]
    if command == 'InsertSpace':
        my_index = int(line.split(':|:')[1])
        message = message[:my_index] + ' ' + message[my_index:]
        print(message)

    elif command == 'Reverse':
        subs = line.split(':|:')[1]
        if subs in message:
            message = message.replace(subs, '', 1)
            message += subs[::-1]
            print(message)
        else:
            print('error')

    elif command == 'ChangeAll':
        old_ch = line.split(':|:')[1]
        new_ch = line.split(':|:')[2]
        if old_ch in message:
            message = message.replace(old_ch, new_ch)
            print(message)

    line = input()

print(f'You have a new text message: {message}')
