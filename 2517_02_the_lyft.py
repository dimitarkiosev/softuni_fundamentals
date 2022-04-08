people = int(input())
lift = list(map(int,input().split(" ")))
index = 0

while people > 0:
    if index <= len(lift) - 1:
        needed = 4 - lift[index]
        if people >= needed:
            lift[index] = lift[index] + needed
            people = people - needed
        else:
            lift[index] = lift[index] + people
            people = 0
    else:
        break
    index += 1

if lift[-1] == 4 and people == 0:
    print(" ".join(list(map(str,lift))))
elif people == 0:
    print(f'The lift has empty spots!')
    print(" ".join(list(map(str,lift))))
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(list(map(str,lift))))
