def represent_data(data, last_ind):
    result = [x for x in data if x == 0]
    print(f"Cupid's last position was {last_ind}.")
    if len(result) != len(data):
        diff = len(data) - len(result)
        print(f"Cupid has failed {diff} places.")
    else:
        print(f"Mission was successful.")


def cupid(data):
    cur_index = 0
    cupid_last_pos = 0

    while True:
        command = input().split(" ")
        if command[0] == 'Love!':
            break

        my_index = int(command[1]) + cur_index
        if my_index >= len(data):
            my_index = 0

        if -1 < my_index < len(data):
            if data[my_index] > 0:
                data[my_index] -= 2
                if data[my_index] == 0:
                    print(f"Place {my_index} has Valentine's day.")
            else:
                print(f"Place {my_index} already had Valentine's day.")

        cur_index = my_index
        cupid_last_pos = my_index
    represent_data(data, cupid_last_pos)

my_list = list(map(int, input().split('@')))
cupid(my_list)
