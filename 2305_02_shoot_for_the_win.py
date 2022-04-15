targets = list(map(int, input().split(" ")))
command = input()
tar = 0

while command != 'End':
    ind = int(command)
    if 0 <= ind < len(targets):
        value = targets[ind]
        if value != -1:
            for i in range(len(targets)):
                if i != ind:
                    if targets[i] != -1:
                        if targets[i] > value:
                            targets[i] -= value
                        else:
                            targets[i] += value
                else:
                    targets[i] = -1
            tar += 1
    command = input()

print(f'Shot targets: {tar} -> {" ".join(str(each) for each in targets)}')
