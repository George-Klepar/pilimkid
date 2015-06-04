__author__ = 'obir'
# -*- coding: utf-8 -*-

word = 'Потолок'
vowel_set = ('а','е','ё','и','й','о','у','э','ю','я')
vowel_set_found = []
vowel_found_pos = []
pos = 0

for anyletter in word:
    pos = pos + 1
    for anyvowel in vowel_set:
        if anyletter == anyvowel:
            vowel_set_found.append(anyletter)
            vowel_found_pos.append(pos)


print (word)

print (vowel_set_found)
print (vowel_found_pos)

print ("Length: ",end = "")
print (len(vowel_set_found))
