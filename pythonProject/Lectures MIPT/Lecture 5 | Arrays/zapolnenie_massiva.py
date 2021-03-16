A = [0] * 10
top = 0
x = int(input("введи число"))

while x != 0:
    A[top] = x
    top += 1
    x = int(input("введи число"))

for k in range(top-1, -1, -1):
    print(A[k])

print(A)
