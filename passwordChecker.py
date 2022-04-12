import re
def passwordChecker(password):
    steps = 0
    if len(password)>=6:
        for i in range(len(password)):
            if i == len(password) - 1:
                pass
            else:
                if password[i] == password[i + 1] and password[i + 1] == password[i + 2]:
                    steps += 1
                    return steps
    else:
        steps = steps + (6-len(password))
        return steps

    if len(password)<=20:
        for i in range(len(password)):
            if i == len(password) - 1:
                pass
            else:
                if password[i] == password[i + 1] and password[i + 1] == password[i + 2]:
                    steps += 1
                    return steps
    else:
        steps+= len(password)-20
        return steps





    if re.search('[A-Z]', password):
        pass
    else:
        steps += 1

    if re.search('[a-z]', password):
        pass
    else:
        steps+=1

    if re.search('[0-9]', password):
        pass
    else:
        steps += 1

    return steps



print(passwordChecker('aaa111'))