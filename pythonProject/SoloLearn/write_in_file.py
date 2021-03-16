"""Запись массива в файл и вывод каждого элемента с новой строки"""

names = ["John", "Oscar", "Jacob"]

file = open("write_in_file", "w+")
for i in range(len(names)):
    file.write(names[i]+"\n")
file.close()

file= open("write_in_file", "r")
t=file.read()
print (t)
file.close()