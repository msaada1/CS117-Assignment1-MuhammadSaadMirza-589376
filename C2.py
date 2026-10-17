# Calculates the equivalent resistance of resistors in parallel combination

def parallel_resistance(resistors):
    req = 0

    for resistance in resistors:
        req += 1 / resistance

    return round(1 / req, 2)


def test():
    result1 = parallel_resistance([10, 10])
    print(f"Result 1 = {result1}")

    result2 = parallel_resistance([100, 200, 300])
    print(f"Result 2 = {result2}")


test()