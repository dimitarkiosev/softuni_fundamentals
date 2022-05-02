items = input().split("|")
line = input()

while line != 'Yohoho!':
    command = line.split(" ")[0]
    if command == 'Loot':
        for i in range(1,len(line.split(" "))):
            item = line.split(" ")[i]
            if item not in items:
                items.insert(0,item)
    elif command == 'Drop':
        ind = int(line.split(" ")[1])
        if 0 <= ind < len(items):
            items.pop(ind)
    elif command == 'Steal':
        lines = line.split(" ")
        if len(lines) == 1:
            items.pop(len(items)-1)
        else:
          pass
    line = input()

print(", ".join(items))
