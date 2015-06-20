def cyr2lat(a):
    letdict = {'�': 'A', '�': 'B', '�': 'V', '�': 'G', '�': 'D', '�': 'E', '�': 'E', '�': 'Zh', '�': 'Z', '�': 'I',
               '�': 'Y', '�': 'K', '�': 'L', '�': 'M', '�': 'N', '�': 'O', '�': 'P', '�': 'R', '�': 'S', '�': 'T',
               '�': 'U', '�': 'F', '�': 'H', '�': 'Ts', '�': 'Ch', '�': 'Sh', '�': 'Sch', '�': '', '�': 'Y', '�': '',
               '�': 'E', '�': 'Yu', '�': 'Ya', '�': 'a', '�': 'b', '�': 'v', '�': 'g', '�': 'd', '�': 'e', '�': 'e',
               '�': 'zh', '�': 'z', '�': 'i', '�': 'y', '�': 'k', '�': 'l', '�': 'm', '�': 'n', '�': 'o', '�': 'p',
               '�': 'r', '�': 's', '�': 't', '�': 'u', '�': 'f', '�': 'h', '�': 'ts', '�': 'ch', '�': 'sh', '�': 'sch',
               '�': '', '�': 'y', '�': '', '�': 'e', '�': 'yu', '�': 'ya'}
    b = list(a)
    for x in b:
        pos = b.index(x)
        if letdict.get(x):
            b.remove(x)
            b.insert(pos, letdict.get(x))
    return ''.join(b)


i = input()
print(cyr2lat(i))