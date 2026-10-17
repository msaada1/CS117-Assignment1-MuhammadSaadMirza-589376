"""
displays digits on the basis of user's input as followed


black = 0, brown = 1, red = 2, orange = 3, yellow = 4, green = 5, blue = 6, violet = 7, grey = 8, white = 9. For any other input print "Invalid colour".
"""

color = input("Enter Band Color: ")
color = color.lower()

if color == "black":
    print("digit = 0")
elif color == "brown":
    print("digit = 1")
elif color == "red":
    print("digit = 2")
elif color == "orange":
    print("digit = 3")
elif color == "yellow":
    print("digit = 4")
elif color == "green":
    print("digit = 5")
elif color == "blue":
    print("digit = 6")
elif color == "violet":
    print("digit = 7")
elif color == "grey":
    print("digit = 8")
elif color == "white":
    print("digit = 9")
else:
    print("Invalid color")
