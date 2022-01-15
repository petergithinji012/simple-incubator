import random
while True:
    egg_size=input("Enter the egg_size:").lower()

    if egg_size=="small":
        print("This is a hen's egg")
    elif egg_size== "medium":
            print("This a duck's egg")
    elif egg_size=="large":
                print("This is a goose egg")


    eggs_colour=input("Enter the egg colour:")

    if eggs_colour=="yellow":
        print("The egg is fertilised and ready for hutching")
    elif eggs_colour=="pale_yellow":
            print("The egg cannot be hutched")
