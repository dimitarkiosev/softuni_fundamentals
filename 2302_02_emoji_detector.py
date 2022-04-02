import re
my_text = input()

matches = re.findall(r'\d' , my_text)

cool_target = 1
for each in matches:
    cool_target = cool_target * int(each)
print(f'Cool threshold: {cool_target}')

expresion = r'(?P<sur>\:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1'
matches = re.findall(expresion, my_text)
print(f'{len(matches)} emojis found in the text. The cool ones are:')

matches = re.finditer(expresion, my_text)
for match in matches:
    emoji_value = 0
    sur = match.group("sur")
    emoji = match.group("emoji")
    for ch in emoji:
        emoji_value += ord(ch)
    if emoji_value > cool_target:
        print(f'{sur}{emoji}{sur}')
