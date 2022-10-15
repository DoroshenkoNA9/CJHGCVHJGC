def stroka(slovo):
    slovo = str(slovo)

    if '!' in slovo:
        slovo = slovo
    else:
        slovo = slovo+ '!'

    return(slovo.capitalize())

print(stroka('привет мир'))