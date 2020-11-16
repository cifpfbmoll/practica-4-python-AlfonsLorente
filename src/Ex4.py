#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario tres números y un cuarto número, y compruebe si este último es divisor de los tres números primeros

if __name__ == "__main__":
    #ask the numbers
    num1 = float(input("insert a numeber: "))
    num2 = float(input("insert a numeber: "))
    num3 = float(input("insert a numeber: "))
    div = float(input("insert one last number: "))
    #print if its divisor or not
    if(num1 % div == 0 and num2 % div == 0and num3 % div == 0):
        print("The last number (", div,") is a divisor of the numbers: ", num1,", ", num2," and ", num3)
    else:
        print("The last number (", div,") is NOT a divisor of the numbers: ", num1,", ", num2," and ", num3)
