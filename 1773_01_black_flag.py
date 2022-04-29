days = int(input())
plunder = int(input())
exp_plunder = float(input())

total = 0
count = 1
while count <= days:
    total += plunder
    if count % 3 == 0:
        total += (plunder*0.5)
    if count % 5 == 0:
        total = total * 0.7

    count += 1

if total >= exp_plunder:
    print(f'Ahoy! {total:.2f} plunder gained.')
else:
    print(f'Collected only {((total/exp_plunder)*100):.2f}% of the plunder.')
