import math
weight = int(input("what's your weight?\n"))
unit = input("(L)lbs or K(kg)\n").lower()
if unit == "l":
    converted = weight * 0.45
    print(f"your weight is {converted} kgs")
elif unit == "k":
    converted = weight // 0.45
    print(f"your weight is {converted} lbs")
else:
    print("N/A")
