def PalidromNumRead(x):
    nx = str(x)
    rn = []
    count = 0
    if x >= 0:
        for i in range(len(nx) - 1, -1, -1):
            rn.append(nx[i])

        for i in range(len(nx)):
            if nx[i] == rn[i]:
                count += 1
    if count == len(nx):
        return True
    else:
        return False

def EnterTheNum ():
    x = int(input("enter the number : "))
    return x

number = EnterTheNum()
result = PalidromNumRead(number)
print(result)



