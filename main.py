N = int(input("Введите размер списков: "))

A = []
print("Введите элементы списка A: ")
for i in range(N):
    e = int(input())
    A.append(e)

B = []
print("Введите элементы списка B: ")
for i in range(N):
    e = int(input())
    B.append(e)

C = []
for i in range(N):
    C.append(A[i] + B[i])

print("Список C (сумма элементов):", C)
