# -*- coding: utf-8 -*-
import re

# Sentence to separate words splitting function
def s2w (input_string):
    ret = re.sub('\W',' ', input_string).split()
    return ret


#words to syllables block

vowels = set(u'аеёиоуыэюя')
sign_chars = set(u'ъь')
pattern_str = u"(c*[ьъ]?vc+[ьъ](?=v))|(c*[ьъ]?v(?=v|cv))|(c*[ьъ]?vc[ъь]?(?=cv|ccv))|(c*[ьъ]?v[cьъ]*(?=$))"
pattern = re.compile(pattern_str)

def get_syllables(word):
  mask = ''.join(['v' if c in vowels else c if c in sign_chars else 'c' for c in word.lower()])
  return [word[m.start():m.end()] for m in pattern.finditer(mask)]


# Sentence splitting demo with function "s2w"

print(u'Введите строку: ',end="")
sentence = input()
wordsArray = s2w(sentence)

# Print result

for i in wordsArray:
    print ('-'.join(get_syllables(i))+" ",end="")