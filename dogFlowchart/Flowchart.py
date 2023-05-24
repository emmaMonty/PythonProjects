print("Is it an object [y/n]?")
response = input()
if response == "n":
    print("Is it a sound [y/n]")
    response1 = input()
    if response1 == "y":
        print("Bark at it")
    else:
        print("Ignore it")
else:
    print("Can you eat it [y/n]?")
    response2 = input()
    if response2 == "n":
        print("Is it a tennis ball [y/n]?")
        response3 = input()
        if response3 == "y":
            print("Pick it up")
            print("Return to owner")
        else:
            print("Bark at it")
    else:
        print("Eat it")
        print("Was it good [y/n]?")
        response4 = input()
        if response4 == "y":
            print("Wag your tail")
        else:
            print("Puke it out")
            print("Re-eat it")
