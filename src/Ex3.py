#!/usr/bin/env python3
#encoding: windows-1252
# Pida al usuario si quiere calcular el área de un triángulo o un cuadrado, y pida los datos según que caso y muestre el resultado.

if __name__ == "__main__":
    #Ask if he wants to calculate a triangle area or an square area
    print("What area do you want to calculate (press: 1 or 2)")
    answer = int(input("1.Triange\n2.Square\n"))
    #calculate the triangle area
    if answer == 1:
        b = float(input("Base: "))
        h = float(input("High: "))
        area = (b*h)/2
        print("The area of the triangle is: ", "%.2f"%area)
    #calculate the square area
    elif( answer == 2):
        side = float(input("Side length: "))
        side *= side
        print("The area of the square is: ", "%.2f"%side)
    #if the choosed option is wrong
    else:
        print("Incorrect option")
