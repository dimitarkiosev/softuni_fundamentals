import re
my_num = int(input())

for _ in range(my_num):
    product_group = ''
    my_text = input()
    expresion = r"\@\#+(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])\@\#+"
    matches = re.findall(expresion, my_text)

    if matches:
        barcode = matches[0]
        char = ''
        for ch in barcode:
            if ch.isdigit():
                product_group += ch
        if product_group == '':
            product_group = '00'
        print(f'Product group: {product_group}')
    else:
        print(f'Invalid barcode')
