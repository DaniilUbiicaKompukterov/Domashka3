# 1-е задание
myList = [1, 2, 3]                  # числа
myNewList = [i * 2 for i in myList] # умножение чисел на 2
print(myNewList)                    # вывод новых чисел


# 2-е задание
mylist = [1,2,3]  # числа
counter = 0       # счетчик   
for i in mylist:  # цикл 
    counter+=i*i  # числа записываются в счётчик в квадрате и складываются
print(counter)    # вывод нового числа




# 3-е задание
list = 'Hello world'                                      # текст
for i in range(len(list)):                                # цикл по индексам
    if list[i] == " ":                                    # поиск пробела 
        list = list.replace("Hello world", "HELLO WORLD") # если пробел есть , то всё преходит в верхний регистр
print(list)                                               # вывод результата


# 4-е задание

for i in range(1900, 2021):           # диапозон годов
    print(i)                          # вывод


