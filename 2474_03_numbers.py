my_list = list(map(int,input().split(" ")))

av_el = sum(my_list) / len(my_list)

list1 = list(filter(lambda x : x > av_el, my_list))

if len(list1) == 0:
    print('No')

list1.sort(reverse=True)

if len(list1) > 5:
    list2 = [str(list1[each]) for each in range(5)]
    print(" ".join(list2))
else:
    print(" ".join([str(each) for each in list1]))
