A=[1,2,3,4,4]
i=0
d=0
if len(A)%2==1:
	i=(len(A)+1)//2
	A.remove(A[i-1])
else :
	i=len(A)//2
	A.remove(A[i-1])
	d=len(A)//2 +1
	A.remove(A[d-1])
	
print(A)