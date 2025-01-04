print("Welcome to wallet balance calculator")
intial=float(input("How much money you have\n"))
expp=[]
earnn=[]

while intial!=0:
    x=float(input("Enter expense or recieved\n"))
    intial=intial+x
    exp=0
    earn=0
    if x<0 :
            exp+=x
            expp.append(exp)
    else  :
            earn+=x
            earnn.append(earn)

    totex=sum(expp)
    toter=sum(earnn)
    print("Your balance is",intial)
    print("your total expneses is",totex)
    print("your total earning is",toter)
print("\n")