# Calculates unloaded and loaded output voltage of a voltage divider

def loaded_divider(vs, r1, r2, rl):
    req1 = (r2 * rl) / (r2 + rl)

    unloaded = vs * r2 / (r1 + r2)
    loaded = vs * req1 / (r1 + req1)

    return (round(unloaded, 2), round(loaded, 2))


def test():
    print(loaded_divider(12, 1000, 1000, 500))


test()