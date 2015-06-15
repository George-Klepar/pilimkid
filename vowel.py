import re

vowel_set = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
I = 'i'
X = 'ь'

#Возврат списка позиций гласных в слове. Может вернуть так же список самих гласных vowel_set_found
#и количество гласных len(vowel_set_found)
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

def str2word (sentence):
    spl = re.split('\W+', sentence)
    spl2 = []
    for anyword in spl:
        spl2.append(azirivka(anyword))
    spl3 = " ".join(spl2)
    return spl3

#меняет все гласные на i. Тестовая функция
def x_repl(slovo):
    new_slovo=slovo
    temp_slovo = list(new_slovo)
    fvowels = findvowels(slovo)
    for i in fvowels:
        temp_slovo[i-1] = u'i'
    return temp_slovo

#Проверка на гласность буквы
def checkifvowel(letter):
    result = False
    for element in vowel_set:
        if letter == element:
            result = True
    return result

#Объединяет элементы списка в строку list - > string
def listtostring(input_list):
    result = ''.join(input_list)
    return result


def azirivka(slovo):
    temp_slovo = list(slovo)
    fvowels = findvowels(slovo)

    #если 2 слога и последняя гласная, меняем первую гласную
    if (len(fvowels) == 2) and (checkifvowel(slovo[len(slovo)-1]) == True):
        temp_slovo[fvowels[0]-1] = I

    # Если два слова и последняя согласная, меняем вторную гласную
    if (len(fvowels) == 2) and (checkifvowel(slovo[len(slovo)-1]) == False):
        temp_slovo[fvowels[1]-1] = I

    #если один слог
    if (len(fvowels) == 1) and (len(temp_slovo)>2):
        temp_slovo[fvowels[0]-1] = I
    elif (len(temp_slovo) <= 2):
        print (slovo)

    #если третий слог, меняем 2-ую + если посл.согласная меняем 3-юю
    if (len(fvowels) == 3):
        temp_slovo[fvowels[1]-1] = I
        if (checkifvowel(slovo[len(slovo)-1]) == False):
            temp_slovo[fvowels[2]-1] = I
        if (temp_slovo[fvowels[1]-2] == X) or (temp_slovo[fvowels[2]-2] == X):
            temp_slovo.pop(fvowels[1]-2)
            
    if (len(fvowels) == 4):
        temp_slovo[fvowels[2]-1] = I
        temp_slovo[fvowels[1]-1] = I
        
    if (len(fvowels) == 5):
        temp_slovo[fvowels[3]-1] = I
        temp_slovo[fvowels[2]-1] = I
        temp_slovo[fvowels[1]-1] = I

    if (len(fvowels) == 6):
        temp_slovo[fvowels[4]-1] = I
        temp_slovo[fvowels[3]-1] = I
        temp_slovo[fvowels[2]-1] = I
        temp_slovo[fvowels[1]-1] = I
        
    return listtostring(temp_slovo)
