# 1-е задание
myList = [1, 2, 3]
myNewList = [i * 2 for i in myList]
print(myNewList)


# 2-е задание
myList = [1, 2, 3]
myNewList = [i ** 2 for i in myList]
print(myNewList)




# 3-е задание
list = 'Hello world'
for i in range(len(list)):
    if list[i] == " ":
        list = list.replace("w", "W")
print(list)


# 4-е задание
from datetime import datetime

year1 = datetime.now().year
year2 = 1900
ren = year1 - year2
for i in range(ren+1):
    print(year2 + i)


