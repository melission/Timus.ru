import sys

char_count = int(input())
chars = []
letters = []
for char in sys.stdin:
    char = char.strip()
    if len(char) > 1:
        chars.append(char)
    elif len(char) == 1:
        letters.append(char)
chars.sort()
letters.sort()
for letter in letters:
    for frst_letter in chars:
        if frst_letter[0] == letter:
            print(frst_letter)
