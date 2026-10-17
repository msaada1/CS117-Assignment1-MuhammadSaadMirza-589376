"""
asks for bits from user and gives the resultant AND OR and XOR logic gates outputs

"""

bit_1 = int(input("Enter A: "))
bit_2 = int(input("Enter B: "))

if bit_1 != 1 and bit_1 != 0 or bit_2 != 1 and bit_2 != 0:
    print("Bits must be 0 or 1")
else:
    #-- And
    if bit_1 == 1 and bit_2 == 1:
        and_output = 1
    else:
        and_output = 0

    #--Or
    if bit_1 == 1 or bit_2 == 1:
        or_output = 1
    else:
        or_output = 0

    #--Xor
    if bit_1 != bit_2:
        xor_output = 1
    else:
        xor_output = 0

    print(f"AND = {and_output}")
    print(f"OR = {or_output}")
    print(f"XOR = {xor_output}")



