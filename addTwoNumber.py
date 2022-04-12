'''
l1 = [1,5,6,1,5,5,1]
l2 = []
for i in range(len(l1)-1, 0, -1):
    l2.append(l1[i])
    
l1.reverse()
print(l1)
'''

def addTwoNumbers(l1, l2):
    l3 = []
    l4 = []
    for a in range(len(l1)-1, 0, -1):
        l3.append(l1[a])
    for b in range(len(l2)-1, 0, -1):
        l4.append(l2[b])

    x = 0
    for i in range(len(l3)):
        for j in range(len(l4)):
            if l3[i] + l4[j] > 9:
                print(0)
            
            x = l3[i] + l4[j]
            print(x)


print(addTwoNumbers([2,4,3],[5,6,4]))