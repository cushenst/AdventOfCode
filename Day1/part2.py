total = 0


def fuelForFuel(mass):
    total = 0
    while mass > 0:
        mass = mass // 3
        mass -= 2
        if mass > 0:
            total += mass
    return total

for i in range(100):
    mass = int(input())
    mass = mass // 3
    mass -= 2
    mass += fuelForFuel(mass)
    total += mass

print(total)
