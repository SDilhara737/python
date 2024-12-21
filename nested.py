



#dicationarry
student={"sfe001":{"name":"Amal","age":20},
         "sfe002":{"name":"Bimal","age":23}
}

z=input("Enter your index numb\n")
print("Your details are below:")
print(student[z])

#tupple
person=(("Sam",50),("Kara",20),("Sai",60))
#unpack tupple

p1,p2,p3=person #unpack main tupple

name1,age1=p1
name2,age2=p2
name3,age3=p3 # unpack sub tupples

print(name3)


