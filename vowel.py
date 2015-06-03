__author__ = 'obir'
# -*- coding: utf-8 -*-

word = u"Гидроэлектростанция"
print (word)

vowel_set = ('а','е','ё','и','й','о','у','э','ю','я')
vowel_set_found = []
pos = 0

for anyletter in word:
    for anyvowel in vowel_set:
        if anyletter == anyvowel:
            vowel_set_found.append(anyletter)
            vowel_set_found.append(pos)


print (vowel_set_found)
print (len(vowel_set_found))

