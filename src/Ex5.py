#!/usr/bin/env python3
#encoding: windows-1252

#Pida al usuario un importe en euros y diga si el cajero autom�tico le puede dar dicho importe utilizando el mismo billete y el m�s grande 	
#(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 �).
#Por ejemplo: 
#25 euros �el cajero te devuelve 5 billetes de 5 euros�	
#20 euros �el cajero te devuelve 1 billete de 20 euros�
#130 euros �el cajero te devuelve 13 billetes de 10 euros�

if __name__ == "__main__":
    #ask for the money
    money = int(input("How many money do you want?: "))
    #make a list with all the bills
    moneylist = [500, 200, 100, 50, 20, 10, 5]
    #if the money is equal to one of the available bills
    if(money == moneylist[0] or money == moneylist[1] or money == moneylist[2] or money == moneylist[3] or \
    money == moneylist[4] or money == moneylist[5] or money == moneylist[6]):
        print("The casher gives you back ", money, "�")
    #if the bill is divisible of money, give back the necesary bills
    elif(money % moneylist[0] == 0):
        print("The casher gives you back", int(money/moneylist[0]), " bills of ", moneylist[0], "�")
    elif(money % moneylist[1] == 0):
        print("The casher gives you back", int(money/moneylist[1]), " bills of ", moneylist[1], "�")
    elif(money % moneylist[2] == 0):
        print("The casher gives you back", int(money/moneylist[2]), " bills of ", moneylist[2], "�")
    elif(money % moneylist[3] == 0):
        print("The casher gives you back", int(money/moneylist[3]), " bills of ", moneylist[3], "�")
    elif(money % moneylist[4] == 0):
        print("The casher gives you back", int(money/moneylist[4]), " bills of ", moneylist[4], "�")
    elif(money % moneylist[5] == 0):
        print("The casher gives you back", int(money/moneylist[5]), " bills of ", moneylist[5], "�")
    elif(money % moneylist[6] == 0):
        print("The casher gives you back", int(money/moneylist[6]), " bills of ", moneylist[6], "�")
    #the money cant have coins
    else:
        print("ERROR: Cant give you coins, only bills")

