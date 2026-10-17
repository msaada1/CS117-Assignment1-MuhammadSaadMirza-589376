#gives current for a fixed resistance for V =1 to V = 10

    # ----Resistance----
r = 10

    # ---- Loop for voltage---
for v in range(1, 11):
    # --- Finding Current ---
    i = v / r
    # ---- Final Output
    print(f" V = {v} V, I = {i} A")


