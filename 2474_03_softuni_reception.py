import math

emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())
st_count = int(input())

for_hour = emp_1 + emp_2 + emp_3

hours = math.ceil(st_count / for_hour)

if hours % 3 == 0:
    breaks = (hours // 3) - 1
else:
    breaks = hours // 3

all_hours = hours + breaks

print(f'Time needed: {all_hours}h.')
