
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