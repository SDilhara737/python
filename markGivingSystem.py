
x=int(input("Enter your mark\n"))

'''if x<100 and x>=75:
    print("Your grade is 'A'")

if x < 75 and x >= 65:
    print("Your grade is 'B'")

if x<65 and x>=55:
    print("Your grade is 'C'")

if x<55 and x>=40:
    print("Your grade is 'D'")

if x<40:
    print("Your grade is 'E'")'''

    #better way to do above

if x<40:
    print("Your grade is 'E'")

elif x <= 54:
    print("Your grade is 'D'")

elif x <= 64:
    print("Your grade is 'C'")

elif x <= 74:
    print("Your grade is 'B'")

elif x <100:
    print("Your grade is 'A'")


else:
    print("out of range")
