#ATM CODE
#variable
Atm_card="card"
pin=1234
money=1000
Temp=0
#code starts
for outer in range(1,3):
    #outer for loop you are a person
    print("you are in front of ATM machine")
    print("Insert your card")
    print("Enter your pin")
    #if
    if (Atm_card == "card") & (pin==1234): #True
        #Nested if
        if outer== 1: #2 == 1 False
            #ATM machine
            while Temp <= money: # 0 <= 1000 True
                print( "count",Temp,"Total Amount", money)
                Temp = Temp + 100 #0 100 200 300 400
                print("Take your money",money,"Rupee")
        else:
            print("Only one attempt is possible")
    elif (Atm_card == "card") | (pin == 1234):
        print("Any one value is wrong")
    else:
        print("Both values are wrong")
        print("Thank you for use")



