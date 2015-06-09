# -*- coding: utf-8 -*-

word = u'Параллелепипед'
vowel_set = (u'а', u'е', u'ё', u'и', u'й', u'о', u'у', u'э', u'ю', u'я')
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

print("Length: ",)
print(len(vowel_set_found))