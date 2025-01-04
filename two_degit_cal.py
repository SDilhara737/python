


def add():
    print("Enter two values to get summation")
    x=int(int(input("Enter first number")))
    y = int(int(input("Enter second number")))
    print('Result: ',x+y)

def min():
    print("Enter two values to get Result")
    x = int(int(input("Enter first number")))
    y = int(int(input("Enter second number")))
    print('Result: ',x-y)

def mul():
    print("Enter two values to get result")
    x = int(int(input("Enter first number")))
    y = int(int(input("Enter second number")))
    print('Result: ',x*y)
def div():
    print("Enter two values to get result")
    x = int(int(input("Enter first number")))
    y = int(int(input("Enter second number")))
    print('Result: ',x/y)

inp=input("Enter function you want to perform\n+ =addition\n- =minus\n* =multiplication\n/ =division\n\nEnter operation here_")

if  inp=='+':
    add()

elif inp=='-':
    min()

elif inp=='*':
    mul()

elif inp=='/':
    div()