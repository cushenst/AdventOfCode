rawInput = input()
listInput1 = list(map(int, rawInput.split(",")))
for a in range(100):
    for b in range(100):
        listInput = [x for x in listInput1]
        listInput[1] = a
        listInput[2] = b
        i = 0
        while True:
            opcode = listInput[i]
            i1,i2,i3 = listInput[i+1], listInput[i+2], listInput[i+3]
            if opcode == 1:
                listInput[i3] = listInput[i1] + listInput[i2]
            elif opcode == 2:
                listInput[i3] = listInput[i1] * listInput[i2]
            elif opcode == 99:
                break
            i += 4
        if listInput[0] == 19690720:
                print(a, b)

