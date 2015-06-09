# -*- coding: utf-8 -*-

def findvowels(sword):
    vowel_set = (u'а', u'е', u'ё', u'и', u'й', u'о', u'у', u'э', u'ю', u'я')
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
    return [vowel_set_found, vowel_found_pos, len(vowel_set_found)]