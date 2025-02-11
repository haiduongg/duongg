A=[1,2,3,4,5,4,8,6,5,5]
max=A[len(A)-1]

for i in range(len(A)):

     if(A[i]<max):

        max=i

print("Giá trị nhỏ nhất của dãy A: ", A[max])

print("Chỉ số là: ", max) 