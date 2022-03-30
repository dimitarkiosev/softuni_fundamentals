mnum = int(input())
all_cars = dict()

for i in range(mnum):
    car_info = input().split('|')
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    if car not in all_cars:
        all_cars[car] = list()
    all_cars[car].append(mileage)
    all_cars[car].append(fuel)

line = input()

while line != 'Stop':
    command = line.split(' : ')[0]
    car = line.split(' : ')[1]
    if command == 'Drive':
        dist = int(line.split(' : ')[2])
        fuel = int(line.split(' : ')[3])
        if all_cars[car][1] < fuel:
            print('Not enough fuel to make that ride')
        else:
            all_cars[car][0] += dist
            all_cars[car][1] -= fuel
            print(f'{car} driven for {dist} kilometers. {fuel} liters of fuel consumed.')
        if all_cars[car][0] >= 100000:
            all_cars.pop(car)
            print(f'Time to sell the {car}!')

    elif command == 'Refuel':
        fuel = int(line.split(' : ')[2])
        need_fuel = 75 - all_cars[car][1]
        if need_fuel > fuel:
            all_cars[car][1] += fuel
            print(f'{car} refueled with {fuel} liters')
        else:
            all_cars[car][1] = 75
            print(f'{car} refueled with {need_fuel} liters')

    elif command == 'Revert':
        reverted_km = int(line.split(' : ')[2])
        all_cars[car][0] -= reverted_km
        if all_cars[car][0] >= 10000:
            print(f'{car} mileage decreased by {reverted_km} kilometers')
        else:
            all_cars[car][0] = 10000

    line = input()

for (car,value) in all_cars.items():
    print(f'{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.')
