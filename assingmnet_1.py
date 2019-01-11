#python assingment one
def age():
    inp = input("Enter the year of birth:")
    fhand = int(inp)
    ned= 2019-fhand
    print(ned)  
age()

#Question 2
marks = [90,34,45,67,12,33,77,88,92,26,69,48,73,5,51,84,56,100,0]
for n in marks:
    if(n>=80):
        print(n,"-D1")
    elif(70<=n<=79):
        print(n,"-D2")
    elif(65<=n<=69):
        print(n,"-C3")
    elif(50<=n<=59):
        print(n,"-C4")
    elif(45<=n<=49):
        print(n,"-C5")
    elif(40<=n<=44):
        print(n,"-C6")
    elif(35<=n<=39):
        print(n,"-Pass")
    else:
        print(n,"faliure")
