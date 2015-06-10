vowel_set = ('а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я')
I = 'i'

def findvowels(sword):
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


#меняет все гласные на i
def x_repl(slovo):
    new_slovo=slovo
    temp_slovo = list(new_slovo)
    fvowels = findvowels(slovo)
    for i in fvowels:
        temp_slovo[i-1] = u'i'
    return temp_slovo

#Проверка, гласная ли буква
def checkifvowel(letter):
    result = False
    for element in vowel_set:
        if letter == element:
            result = True
    return result

#Объединяет элементы списка в строку
def listtostring(input_list):
    result = ''.join(input_list)
    return result


def azirivka(slovo):
    temp_slovo = list(slovo)
    fvowels = findvowels(slovo)

    #тут начинаются правила
    if len(fvowels)==2 and (checkifvowel(slovo[len(slovo)-1])==True):
        temp_slovo[fvowels[0]-1] = I

    if len(fvowels)==1:
        temp_slovo[fvowels[0]-1] = I

    if len(fvowels) == 2 and (checkifvowel(slovo[len(slovo)-1])==False):
        temp_slovo[fvowels[1]-1] = I

    return listtostring(temp_slovo)
