def reverse(x):
    negeative = False
    if x < 0:
        negeative = True
        x *= -1
    a = str(x)
    a = a[::-1]
  
    a = int(a)
    if negeative == True:
        a *= -1
    return a
        

print(reverse(-6551))
