def without_plus(a,b):
    while b!=0:
      	a, b = a^b, (a&b) << 1
    return a
    
x = without_plus(1,8)
print(x)
