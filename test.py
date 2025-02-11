n=int(input("nhập số n:"))
def generate_d(n, a=0, b=1):
    if n < 2:
        return "Độ dài danh sách phải lớn hơn hoặc bằng 2"
    
    d= [a,b]
    
    for i in range(n - 2):
        i = d[-1] + d[-2]
        d.append(i)
    return d
    
    

print(generate_d(n))