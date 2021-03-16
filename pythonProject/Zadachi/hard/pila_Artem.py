inp = open("Saw input.txt", 'r')

# reads a file by strings and converts second one in an list of integers

base_list = inp.readline()
base_list_int = list((int(a) for a in (inp.readline().split())))

# ***

# some auxiliary vars and empty lists

sign_list = []
y = len(base_list_int)
test_list = []
to_exit = False


# ***

# finds 3 numbers corresponding to condition

def triple(a, b, c):
    if base_list_int[a] < base_list_int[b] > base_list_int[c] or \
            base_list_int[a] > base_list_int[b] < base_list_int[c]:
        return True


# ***

# checks for correct incoming data

if y < 3:
    print('Incorrect input')
    exit(ImportError)

# ***

# checks trivial cases

if y == 3:
    if base_list_int[0] == base_list_int[1] == base_list_int[2]:
        print('Answer is 1')
    elif triple(0, 1, 2):
        print('Answer is 3')
    else:
        print('Answer is 2')
    exit(Exception)

# *

if all(x == base_list_int[0] for x in base_list_int):
    print('Answer is 1, all of the elements are the same')
    exit(Exception)

# ***

i = 1
j = 0

while j <= y - 3:
    print('j = ', j, ',значение счётчика j, вход в первый цикл')
    if triple(j, j + 1, j + 2):
        print('j = ', j, 'первый цикл нашёл триплет')
        test_list.insert(j, base_list_int[j:j + 3])

        print(test_list, ' --- list with subsequences;')
        i = j + 1
        print('i = ', i, ', вход во второй цикл')
        while i >= j + 1:
            if triple(i, i + 1, i + 2):
                print('j = ', j, 'найден второй триплет, начало второго цикла')
                print(test_list, ' --- list with subsequences;')
                if i + 3 >= y:
                    test_list.insert(j, base_list_int[j:])
                    print(test_list, ' --- list with subsequences;')
                    to_exit = True
                    j = y
                    print('i = ', i, ', конец всей последовательности')
                    print(test_list, ' --- list with subsequences;')
                    print('to_exit')
                    break
                else:
                    test_list.insert(j, base_list_int[j:i + 3])

                    print('i = ', i, ', продолжение второго цикла')
                    print(test_list, ' --- list with subsequences;')
                    i += 1
                continue

            else:
                test_list.insert(j + 1, '')

                j = i + 1
                print('j = ', j, ', продолжение проходки по основной последовательности, второй цикл не нашёл триплета')
                print(test_list, ' --- list with subsequences;')
                break
#        if to_exit:
#            j = y
#            break
#        j = i + 1
#    elif j + 1 == y - 1:
#        to_exit = True
#        j = y - 2
#        break
    else:
        print('j = ', j, ', первый цикл не нашёл триплета')
        test_list.insert(j, '')

        print(test_list, ' --- list with subsequences;')
        j += 1

# ***

for i in range(0, len(test_list)):
    sign_list.append(len(test_list[i]))

# ***

# final exception fo list like [1, 1, 1, 2, 2, 2]

if sign_list == [] or max(sign_list) == 0:
    print('Answer is 2')
    exit(Exception)

# *************************************

# outputs some intermediate information and final answer

print('_______________________________________')
print('_______________________________________')
print(base_list_int, ' --- original sequence;')
print('_______________________________________')
print('_______________________________________')
print(test_list, ' --- list with subsequences;')
print('_______________________________________')
print('_______________________________________')
print(sign_list, ' --- lengths of subsequences;')
print('_______________________________________')
print('_______________________________________')
print('Final answer is ', max(sign_list), '.')
inp.close()
