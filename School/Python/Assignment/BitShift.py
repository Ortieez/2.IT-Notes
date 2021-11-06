print("======================================")
print("--BitShift--")
print("This program takes a number\nand shifts it to the left\nor right depending on what you choose")
print("======================================\n\n")

if __name__ == '__main__':
    while True:
        try:
            num = int(input("Insert a number: "))
            offset = int(input("Insert how to many times to shift: "))
            way = int(input("How you want to shift (Left = 0; Right = 1): "))

            if (way == 0):
                num <<= offset
                print("Your new number: " + str(num))
                print("Your new number in binary: " + str(bin(num)))
                exit()
            elif (way == 1):
                num >>= offset
                print("Your new number: " + str(num))
                print("Your new number in binary: " + str(bin(num)))
                exit()
            else:
                print("Something wrong happened please try again!")
                exit()

        except ValueError:
            print("Enter only numbers!\n\n")

        except KeyboardInterrupt:
            print("\n\n\n\nExitting...")
            exit()
