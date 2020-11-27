'''
my_list = [1, 2, 3]
my_new_list = [i * 2 for i in my_list]
print(my_new_list)
'''

'''
my_list = [1, 2, 3]
my_new_list = [i ** 2 for i in my_list]
print(my_new_list)
'''

'''
list = 'Hello world'
for i in range(len(list)):
    if list[i] == " ":
        list = list.replace(list[i + 1], list[i + 1].upper(), 1)
print(list)
'''

'''
list = 'Hello world'
for i in range(len(list)):
    if list[i] == " ":
        list = list.replace("w", "W")
print(list)
'''

'''
from datetime import datetime

year1 = datetime.now().year
year2 = 1900
rad = year1 - year2
for i in range(rad+1):
    print(year2 + i)
'''

