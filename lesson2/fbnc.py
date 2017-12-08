a = 1
b = 1
print(1)
print(1)
for i in range(3,100):
    c = b
    b = a + b
    print (b)
    a = c
print()
print("第99项与第100项的比例为：", a/b)

    
    
