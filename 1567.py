# http://acm.timus.ru/problem.aspx?space=1&num=1567&locale=en
import sys

onetap_letters = ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y', '.', ' ']
twotap_letters = ['b', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z', ',']
threetap_letters = ['c', 'f', 'i', 'l', 'o', 'r', 'u', 'x', '!']
price = 0
splited_sentence = []
for sentence in sys.stdin:
    for word in sentence:
        for letter in word:
           splited_sentence.append(letter)
# print(splited_sentence)


for lett in splited_sentence:
    if lett in onetap_letters:
        price += 1
    if lett in twotap_letters:
        price += 2
    if lett in threetap_letters:
        price += 3

print(price)

