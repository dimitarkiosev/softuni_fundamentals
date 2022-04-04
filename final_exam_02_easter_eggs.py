import re
all_eggs = input()
my_pattern = r'[@#]+(?P<color>[a-z]{3,})[@#]+[^a-zA-Z0-9]*[\/]+(?P<count>[0-9]+)[\/]+'

matches = re.finditer(my_pattern, all_eggs)
for match in matches:
    color = match.group("color")
    count = int(match.group("count"))
    print(f'You found {count} {color} eggs!')
