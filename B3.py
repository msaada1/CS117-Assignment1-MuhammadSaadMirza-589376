# Finds the largest, smallest , above 3.2 and the average of readings

# ---Set of Readings
readings = [3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]

# ---Setting initially
smallest = readings[0]
largest = readings[0]
abv_lim = 0
total = 0

# ---Checking for the true values
for x in readings:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
    if x > 3.2:
        abv_lim += 1

    # ---Sum of Values to calculate average
    total = total + x
# ---Average
average = total / len(readings)

print(f"Readings above 3.2 V: {abv_lim}")
print(f"Highest: {largest} V")
print(f"Lowest: {smallest} V")

# ---- to round off to two dp
print(f"Average: {round(average, 2)} V")

