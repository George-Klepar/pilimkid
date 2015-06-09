# -*- coding: utf-8 -*-
import sys

def findvowels(sword):
    vowel_set = (u'а', u'е', u'ё', u'и', u'о', u'у', u'э', u'ю', u'я')
    vowel_set_found = []
    vowel_found_pos = []
    pos = 0
    for anyletter in sword:
        pos += 1
        for anyvowel in vowel_set:
            if anyvowel == anyletter.lower():
                vowel_set_found.append(anyletter)
                vowel_found_pos.append(pos)
                break
    return vowel_found_pos


def x_repl(slovo):
    new_slovo=slovo
    temp_slovo = list(new_slovo)
    fvowels = findvowels(slovo)
    for i in fvowels:
        temp_slovo[i-1] = u'i'
    for x in temp_slovo:
        x.decode('string-escape')
    return temp_slovo