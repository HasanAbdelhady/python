name = input("enter your name\n")
if len(name) < 3:
    print("name is too short")
elif len(name) > 50:
    print("name is too long")
else:
    print("Your name is accepted")