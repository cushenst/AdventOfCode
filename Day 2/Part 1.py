rawInput = input()
listInput = list(map(int, rawInput.split(",")))

for i in range(0,len(listInput),4):
    if listInput[i] == 1:
        number1 = listInput[listInput[i+1]]
        number2 = listInput[listInput[i+2]]
        listInput[listInput[i + 3]] = number1+number2
    elif listInput[i] == 2:
        number1 = listInput[listInput[i + 1]]
        number2 = listInput[listInput[i + 2]]
        listInput[listInput[i + 3]] = number1 * number2
    elif listInput[i] == 99:
        break
print(listInput)


