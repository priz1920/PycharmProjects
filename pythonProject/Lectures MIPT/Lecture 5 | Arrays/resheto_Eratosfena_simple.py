N = int(input("введи размер массива:"))
A = [True] * N
A[0] = A[1] = False

for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
z = 0
for k in range(N):
    if A[k]:
        print(k, "- простое")
        z += 1
    else:
        print(k, "- составное")

print("\nколичество простых чисел:", z, "\n")

for k in range(N):
    print(k, "-", "простое" if A[k] else "составное")

