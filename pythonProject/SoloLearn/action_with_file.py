file = open("test.txt", "r")

print(file.read(18))
print(file.read(4))
print(file.read(8))
print(file.read())

file.close()