# Calculates current using Ohm's law and checks whether the fuse will blow.

volt = float(input("Enter Voltage (V): "))
res = float(input("Enter Resistance (ohm): "))

if res > 0:
    current = volt / res
    print(f"Current = {current} A")

    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
else:
    print("Invalid Resistance")