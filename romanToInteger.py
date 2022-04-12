def romanToInt(x):
    total = 0
    while True:

        for i in range(len(x)):
            if i < 3:
                if x[i] == 'I' 
                total += 1
                if i != 'I':
                    continue
            elif i == 'IV':
                total = str(total) + '4'
        return total

print(romanToInt('IV'))