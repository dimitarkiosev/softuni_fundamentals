line = input()
total = 0
while line != 'special' and line != 'regular':
    price = float(line)
    if price > 0:
        total = total + price
    else:
        print(f'Invalid price!')
    line = input()

taxes = total * 0.2
final_total = total + taxes
if total == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')

if line == 'special':
    final_total = final_total * 0.9
if total > 0:
    print(f'Total price: {final_total:.2f}$')
