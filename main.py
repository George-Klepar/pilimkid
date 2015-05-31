# -*- coding: utf-8 -*-
import re
import sys

# Sentence to separate words splitting function
def s2w (input_string):
    ret = re.sub('\W',' ', input_string).split()
    return ret


# Sentence splitting demo with function "s2w"

sentence = u"Мы - любим кодить...очень: наприпер 'для примера',как типа этого"
wordsArray = s2w(sentence)

for i in wordsArray:
    print(i)
    

# Request to enter sentence to split and write to list
# stdout function do not carry string to new-line

sys.stdout.write(u'Введите строку: ')
s = input()
print (s2w(s))




# в общем, это почти то же самое, что def split2words, но ты пошел дальше и сделал функцию, я еще далек от изящности кода
# вот ниже нашел код разбиения слов на слоги, так, для заметки
'''
#coding=utf-8
import re
vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern_str = u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))"
pattern = re.compile(pattern_str)

def get_syllables(word):
    mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
    return [word[m.start():m.end()] for m in pattern.finditer(mask)]

word = raw_input(u'слово:').decode('utf-8')
print '-'.join(get_syllables(word))
'''
