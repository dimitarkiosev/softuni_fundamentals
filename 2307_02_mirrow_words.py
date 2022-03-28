import re
my_text = input()
expresion = r"(\@|\#)(?P<word1>[a-zA-Z]{3,})\1{2}(?P<word2>[a-zA-Z]{3,})\1"
matches = re.finditer(expresion, my_text)

words = dict()
word_counts = 0
word_minnor = 0
for match in matches:
    words[word_counts] = list()
    words[word_counts].append(match.group("word1"))
    words[word_counts].append(match.group("word2"))
    if words[word_counts][0] == words[word_counts][1][::-1]:
        word_minnor = 1
    word_counts += 1
if word_counts:
    print(f'{word_counts} word pairs found!')
else:
    print(f'No word pairs found!')

if word_minnor:
    print(f'The mirror words are:')
    print(", ".join(f'{value[0]} <=> {value[1]}' for key,value in words.items() if value[0] == value[1][::-1]))
else:
    print(f'No mirror words!')
