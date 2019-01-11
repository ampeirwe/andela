

    #Assignment two
#Questions one
def numbers():
    ned = list()
    for num in range(2000,3200):
        if(num%7==0):
            if(num%5!=0):
                ned.append(num)
    print(ned)
numbers()



#Question Two
def capitalize():
    inp = input("Enter a word or phrase:")
    ned  = inp.upper()
    print(ned)
capitalize() 

#Question 3
#Question 3
def binary():
    zona = []
    zonka = []
    inp1 = input("Enter a four digit number that is binary")
    zona.append(inp1)
    inp2 = input("Enter a four digit number that is binary")
    zona.append(inp2)
    inp3 = input("Enter a four digit number that is binary")
    zona.append(inp3)
    inp4 = input("Enter a four digit number that is binary")
    zona.append(inp4)
    print("Entered numbers:zona)
    for item in zona:
        ned = len(item)
        if(ned==4):
            inp2 = int(item)
            if(inp2%5!=0):
                zonka.append(inp2)
    print("numbers divisible by 5",zonka)
binary()

#Question 4

def banking():
    deposit1 = int(input("Enter your deposit"))
    deposit2 = int(input("Enter your deposit"))
    withdraw = int(input("Enter the amount you need wo withdraw"))
    
    balance1 = deposit1 + deposit2
    balnce2 = balance1 - withdraw
    print("balance after depositing:",balance1)
    print("balance afeter withdrawing:",balnce2)
banking()


#Question 5
def powers():
    zonka = list()
    for i in range(1,20):
        ned = i**2
        zonka.append(ned)
    ned1 = zonka[0:4]
    print(ned1)
powers()
  
    
    
    


