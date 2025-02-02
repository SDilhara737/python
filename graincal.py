
count_bla=[]
count_whi=[]
print("Grain calculator\n")
N=int(input("Enter number of tiles(N)\n_"))

for i in range(1,N+1):


        if i%2 !=0 :
            count_bla.append(i)

        else:
            count_whi.append(i)

blacktot=[]
whitetot=[]
for x in count_bla:
    a=2**(x-1)
    blacktot.append(a)
for y in count_whi:
    b=2**(y-1)
    whitetot.append(b)

tot1=sum(blacktot)
tot2=sum(whitetot)

print("Number of grains in black tile is: ",tot1)
print("Number of grains in white tile is: ", tot2)

