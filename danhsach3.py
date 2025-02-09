A=[9,2,3,4,5,6,5,6,3,2,3,6,7]
p=[1,2,3]
d=-1
i=0
while i < len(A)-3 and d==-1:
	if A[i]==p[0] and A[i+1]==p[1] and A[i+2]==p[2]:
		d=i
	else:
		i=i+1
if d>=0:
	print ("tìm thấy mẫu "+ str(p)+" tại vị trí " + str(d))
else:
	print (" không tìm thấy mẫu " + str(p))
