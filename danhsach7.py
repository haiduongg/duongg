A=[]
n=int(input("nhập số n:"))
for i in range (n+1):
	if i %2==0:
		A.append(i)
	else :
		i=i+1
print(str(n)+" số chắn đầu tiên là :",A)