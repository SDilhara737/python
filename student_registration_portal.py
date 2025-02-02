print("\nWelcome to student registration portal\n")
student = {}
numbers=[]
choise=int

while choise!=9:
    choise=int(input("\n\nENter 1 to enter a student\nENter 2 to remove a student \nEnter 3 to Display student list\nEnter 4 to update student details\nEnter 9 to exit\n_"))
    if choise==1:
        inp = 1
        count = 0
        while inp == 1:
            count = count + 1
            numbers.append(count)
            def add_stu():
                reg_no = int(input("Enter your registration number:"))
                name = input("Enter your name:")
                age = int(input("Enter your age:"))
                city = input("Enter your city")

                student[count] = {"Reg_no": reg_no, "Name": name, "Age": age, "City": city}


            add_stu()
            inp = int(input("enter '1' to add another student or '0' to go to main menu\n:"))

    if choise==2:
        print(student)
        x=int(input("\nEnter which student to be removed:"))
        if x in numbers:
            student.pop(x)
        else:
            print("Student is not in the list\n")
        print("Student",x,"removed")
        print("\nThis is the updated student list\n",student)


    if choise==3:
        print("\nThis is the student list\n",student)


    if choise==4:
        print(student)
        upd=int(input("\nwhich student details you want to update"))

        wht=input("What details you need to update(Reg_no/Name/Age/city)")

        if wht == "Name" or "city":
            student[upd][wht] = input("Enter the new value")
        else:

            student[upd][wht] = int(input("Enter the new value"))
        print("This is the new details",student[upd])
