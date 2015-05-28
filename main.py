# Sentence splitting to words function
def split2words (input_string):
    return input_string.split()


sentence = "We Like Code"
wordsArray = split2words(sentence)

# Print result
for i in wordsArray:
    print(i)

# прiвiт дрiже Дiмi, нiжче бiдiм стрiку рiзбiватi на слiва :)

a = input()
b = a.split('[., ]+')
print(b)

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
