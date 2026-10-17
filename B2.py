#Calculates total resistance in series

# ---Getting to know number of resistors in series--

res_no = int(input("How many Resistors? "))

# Defining a variable to store result
total = 0

# ----Input of resistances
for x in range(1, res_no + 1):
    resistance = int(input(f"Enter R{x}: "))
    total = total + resistance

# ---Printing Total resistance---

print(f"Total Resistance: {total} ohm")

