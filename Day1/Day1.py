total = 0
for i in range(100):
    mass = int(input())
    mass = mass // 3
    mass -= 2
    total += mass

print(total)
