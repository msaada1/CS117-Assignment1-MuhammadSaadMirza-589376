# Calculates current using ohm's law and power dissipated by resistor

def ohms_current(v, r):
    return v / r


def power_dissipated(i, r):
    return i**2 * r


def test():
    v = 12
    r = 6

    current = ohms_current(v, r)
    power = power_dissipated(current, r)

    print(f"Current = {current} A")
    print(f"Power = {power} W")


test()