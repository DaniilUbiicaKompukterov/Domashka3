# 1-е задание
myList = [1, 2, 3]                  # числа
myNewList = [i * 2 for i in myList] # умножение чисел на 2
print(myNewList)                    # вывод новых чисел


# 2-е задание
myList = [1, 2, 3]                   # числа
myNewList = [i ** 2 for i in myList] # возведение чисел во 2-ю степень
print(myNewList)                     # вывод новых чисел




# 3-е задание
list = 'Hello world'                  # текст
for i in range(len(list)):            # цикл по индексам
    if list[i] == " ":                # поиск пробела 
        list = list.replace("w", "W") # если пробел есть , то w меняется на W
print(list)                           # вывод результата


# 4-е задание

for i in range(1900, 2021):           # диапозон годов
    print(i)                          # вывод


