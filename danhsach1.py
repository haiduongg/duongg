d=[]
n=int(input("nhap so n:"))
for i in range(n):
	name=input("nhập tên thứ " + str(i+1) + ":")
	d.insert(0,name)
print("danh sách lớp đã nhập :")
for name in d :
	print(name)