#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario 5 números y diga cuál es el mayor y cuál el menor.

if __name__ == "__main__":
    #declare the variables and ask for the numbers
    num1 = float(input("insert a numeber: "))
    num2 = float(input("insert a numeber: "))
    num3 = float(input("insert a numeber: "))
    num4 = float(input("insert a numeber: "))
    num5 = float(input("insert a numeber: "))
    #Create a list and give it all the numbers
    numlist = [num1, num2, num3, num4, num5]
    #sort the list
    numlist.sort()
    #print the answers
    print("the greater number is:", "%.2f"%numlist[4])
    print("the lowest number is:", "%.2f"%numlist[0])
