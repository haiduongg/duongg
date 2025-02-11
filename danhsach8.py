n=int(input("Nhập số tự nhiên n: "))
i=2

A=[0,1]

F0 = 0

F1 = 1

while i<n:

    m = A[i - 1] + A[i - 2]

    A.append(m)

    i=i+1

print(A)


