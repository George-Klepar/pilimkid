__author__ = 'obir'
# -*- coding: utf-8 -*-

word = 'Параллелепипед'
vowel_set = ('а', 'е', 'ё', 'и', 'й', 'о', 'у', 'э', 'ю', 'я')
vowel_set_found = []
vowel_found_pos = []
pos = 0

for anyletter in word:
    pos += 1
    for anyvowel in vowel_set:
        if anyvowel == anyletter.lower():
            vowel_set_found.append(anyletter)
            vowel_found_pos.append(pos)
            break


print(word)

print(vowel_set_found)
print(vowel_found_pos)

print("Length: ", end="")
print(len(vowel_set_found))
