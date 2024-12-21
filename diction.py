'''
student={
    "name":"A",
    "age":50,
    "mobile":'051515565'
}

print(student)
print(student["age"])

student2={}                  #second method to create a dictionary
student2["name"]="B"
student2["age"]=60
student2["mob nu"]='0484514656'

print(student2)
print(student2["age"])
print(student2.get("age"))

print(student.keys())
print(student.values())
print(student.clear())

student4=()   #this is 3rd method to create a dictionarry
'''

stu=dict(name="C",age=20,contact_no='05656549645')   #4th way to create a dictionarry
print(stu)

stu["city"]="kandy"
print(stu)

stu["age"]=68
print(stu)
