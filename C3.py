# Converts a decimal number to binary without using bin()

def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""

    while n > 0:
        result = n % 2
        binary = str(result) + binary
        n = n // 2

    return binary


def test():
    print(f"decimal_to_binary(10) -> {decimal_to_binary(10)}")
    print(f"decimal_to_binary(25) -> {decimal_to_binary(25)}")


test()