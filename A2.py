#Takes a current value and displays its direction

current = float(input("Enter Value of Current: "))

if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")