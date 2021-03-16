A = [0] * 10
top = 0
n = int(input())

while n != 0:
    A[top] = n
    top += 1
    n = int(input())

H = []
G = []
print(A)

for k in range(top-1, -1, -1):
    H.append(A[k])
for k in range(top):
    G.append(A[k])

print(*H)
print(*G)
