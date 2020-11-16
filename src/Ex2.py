#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario 5 números y diga si estos estaban en orden decreciente, creciente o desordenados.

if __name__ == "__main__":
    #ask for numbers
    num1 = float(input("insert a numeber: "))
    num2 = float(input("insert a numeber: "))
    num3 = float(input("insert a numeber: "))
    num4 = float(input("insert a numeber: "))
    num5 = float(input("insert a numeber: "))
    #Create a list and give it all the numbers
    numlist = [num1, num2, num3, num4, num5]
    #sort the list
    numlist.sort()
    #if the numbers are in ascend order
    if numlist[0] == num1 and numlist[1] == num2 and numlist[2] == num3 and numlist[3] == num4 and numlist[4] == num5:
        print("The numbers are in ascend order")
    #if the numbers are in descendent order 
    elif numlist[0] == num5 and numlist[1] == num4 and numlist[2] == num3 and numlist[3] == num2 and numlist[4] == num1:
        print("The numbers are in descendent order")
    #if the numbers are desordenated
    else:
        print("the numbers are desordenated")