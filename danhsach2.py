A=[1,2,-1,-4,-5,-7,8,9]
i=0
while i < len(A):
	if A[i]  < 0:
		A.remove(A[i])
	else :
		i=i+1
	

	
print(A)