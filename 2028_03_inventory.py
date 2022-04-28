items = input().split(", ")

line = input()

while line != 'Craft!':
    command = line.split(" - ")[0]
    item = line.split(" - ")[1]

    if command == 'Collect':
        if item not in items:
            items.append(item)
    elif command == 'Drop':
        if item in items:
            items.remove(item)
    elif command == 'Combine Items':
        item1 = item.split(":")[0]
        item2 = item.split(":")[1]
        if item1 in items:
            items.insert(items.index(item1)+1,item2)
    elif command == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)

    line = input()

print(", ".join(items))
