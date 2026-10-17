# Finds the smallest and largest input resistances

r1 = int(input("Enter R1: "))
r2 = int(input("Enter R2: "))
r3 = int(input("Enter R3: "))

largest = r1
smallest = r1

if r2 > largest:
    largest = r2

if r3 > largest:
    largest = r3

if r2 < smallest:
    smallest = r2

if r3 < smallest:
    smallest = r3

print(f"Largest = {largest} ohm")
print(f"Smallest = {smallest} ohm")