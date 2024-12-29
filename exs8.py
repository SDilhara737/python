
'''
sym='*'

for x in range(1,6):
    print(sym*x)

spc=' '
for x in range(6):

    print(spc*(5-x)+"*"*x)

for x in range(6):

    print(spc*(5-x)+"*"*x+'*'*(x-1))    '''

spc=' '
for x in range(10):

    if x<6:
    print(spc*(5-x)+"*"*x+'*'*(x-1))

    else:
    print(spc * abs(5 - x) + "*" * x + '*' * abs(x - 1))