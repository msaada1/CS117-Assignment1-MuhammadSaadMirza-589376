# Sorts measured resistors into 1%, 5%, and rejected tolerance groups

resistance = float(input("Enter Measured Resistance: "))

count_1 = 0
count_5 = 0
count_wrong = 0

while resistance != 0:
    if 99 <= resistance <= 101:
        print("1% tolerance")
        count_1 += 1

    elif 95 <= resistance <= 105:
        print("5% tolerance")
        count_5 += 1

    else:
        print("Outside Range")
        count_wrong += 1

    resistance = float(input("Enter Measured Resistance: "))

print(f"1% Tolerance: {count_1}")
print(f"5% Tolerance: {count_5}")
print(f"Rejected/ Outside Range: {count_wrong}")