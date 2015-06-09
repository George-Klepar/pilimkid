# -*- coding: cp1251 -*-

def findvowels(sword):
    vowel_set = (u'а', u'е', u'и', u'о', u'у')
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
        temp_slovo[i-1] = 'i'
    return temp_slovo