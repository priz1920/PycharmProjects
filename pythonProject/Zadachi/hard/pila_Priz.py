import random
a = [5, 7, 6, 3, 4, 2, 7, 1, 8, 9, 4, 5, 5, 5]
b = []
for z in range(10):
    b.append(random.randint(1,2))
a = b

dop_chislo = 0
dlina = 0
i = 1
all_lenght = []
z = 0


while i + 2 <= len(a):
    if (a[i - 1] - a[i]) * (a[i] - a[i + 1]) < 0:
        if i + 2 < len(a):
            dop_chislo += 1
        else:
            dop_chislo += 1
            dlina = 2 + dop_chislo
            all_lenght.append(dlina)
            dop_chislo = 0
    elif dop_chislo > 0:
        dlina = 2 + dop_chislo
        all_lenght.append(dlina)
        dop_chislo = 0
    i += 1



if len(all_lenght) > 0:
    result = max(all_lenght)
    print(result)
else:
    while z < len(a):
        if a[z-1] == a[z]:
            z +=1
        else:
            print("Длина самой длинной пилообразной последовательности: 2")
            break

            #print("нет пилообразных последовательностей")






print(all_lenght)
print(a)