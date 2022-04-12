def sum2(y=[]):
    l2 = []
    for a in range(len(y)-1, -1, -1):
        for b in range(a-1, -1, -1):
            for c in range(b-1, -1, -1):
                if y[a] + y[b] + y[c] == 0:
                    l2.append(y[a])
                    l2.append(y[b])
                    l2.append(y[c])
                    return l2

def sum(x=[]):
    l1 = []
    
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            for k in range(j+1, len(x)):
                if x[i] + x[j] + x[k] == 0:
                    l1.append(x[i])
                    l1.append(x[j])
                    l1.append(x[k])
                    q = sum2(x)
                    return [l1, q]
    



print(sum([-1,0,1,2,-1,-4]))
