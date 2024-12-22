tot=0
students=[]
for x in range(1,4):


    x={"Reg_No":input("Enter your registration number\n"),
        "mark":int(input("Enter your mark"))}

    tot=tot+x["mark"]
    students.append(x)


print(students)
avg=tot/4
print("Total average is: ",avg)


