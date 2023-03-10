#Fibu
x , y = 0 ,1
print(x)
print(y)
for i in range(0,6) :
    print(x + y)
    z = x
    x = y
    y = z + x
