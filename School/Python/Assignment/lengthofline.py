from math import sqrt

a = input("Enter coordinates of A (X,Y): ").split(",")
b = input("Enter coordinates of B (X,Y): ").split(",")

lineA = abs(int(a[0]) - int(b[0])) ** 2
lineB = abs(int(a[1]) - int(b[1])) ** 2

c = round(sqrt(lineA + lineB), 2)

print("Delka usecky od bodu A a B je " + str(c) + " cm")