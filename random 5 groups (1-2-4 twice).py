import random
all_list = ['12', '13', '14', '15', '23', '24', '25', '34', '35', '45']
check = 0

while check == 0:
    check_all = [0,0,0]
    new_list = []
    random.shuffle(all_list)
    for x in range(5):
        if '1' in all_list[x]:
            check_all[0] += 1
        if '2' in all_list[x]:
            check_all[1] += 1
        if '4' in all_list[x]:
            check_all[2] += 1
        new_list.append(all_list[x])
    if check_all[0] > 1 and check_all[1] > 1 and check_all[2] > 1:
        check = 1

print(new_list)
print('check_1:', check_all[0])
print('check_2:', check_all[1])
print('check_4:', check_all[2])
