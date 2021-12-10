while(True):
    try:
        testcase = int(input("Insert any number: "))
        if(testcase % 2 == 0 or testcase % 3 == 0 or testcase % 5 == 0):
            print("Číslo je násobkem alespoň jednoho z čísel 2, 3, 5.")
            exit()
        else:
            print("Číslo není násobkem žádného z čísel 2, 3, 5.")
            exit()
    except ValueError:
        print("Enter a number please.")