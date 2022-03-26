stops = input()

line = input()

while line != 'Travel':
    command = line.split(':')[0]
    if command == 'Add Stop':
        index = int(line.split(':')[1])
        string = line.split(':')[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(f'{stops}')

    elif command == 'Remove Stop':
        start_index = int(line.split(':')[1])
        end_index = int(line.split(':')[2])
        if start_index < len(stops) and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
        print(f'{stops}')

    elif command == 'Switch':
        old_s = line.split(':')[1]
        new_s = line.split(':')[2]
        stops = stops.replace(old_s, new_s)
        print(f'{stops}')
    line = input()

print(f'Ready for world tour! Planned stops: {stops}')
