food = float(input())*1000
hay = float(input())*1000
cover = float(input())*1000
pig_weight = float(input())*1000
days = 1
condition = 1

while days <= 30:
    food -= 300
    if days % 2 == 0:
        hay = hay - (food * 0.05)
    if days % 3 == 0:
        cover = cover - (pig_weight/3)
    if food <= 0 or hay <= 0 or cover <= 0:
        print(f'Merry must go to the pet store!')
        condition = 0
        break
    days += 1

if condition:
    print(f'Everything is fine! Puppy is happy! Food: {(food/1000):.2f}, Hay: {(hay/1000):.2f}, Cover: {(cover/1000):.2f}.')
