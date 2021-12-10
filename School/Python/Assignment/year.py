def checkIfLeap(year):
    if(year % 4 == 0):
        if (year % 100 != 0):
            print("It is leap year")
        elif(year % 400 == 0):
            print("It is leap year")
        else:
            print("It is not leap year")
    else:
        print("It is not leap year")

while(True):
    try:
        checkInput = int(input("Enter year: "))
        checkIfLeap(checkInput)

        tryagain = input("Want again? [Y/N]: ")
        if(tryagain == "Y"):
            continue
        elif(tryagain == "N"):
            exit("\n\n\n\nSee you next time..")
    except ValueError:
        print("Enter a valid number please...")
    except KeyboardInterrupt:
        exit("\n\n\n\nAdios Amigos...")