
print("Hello there,\nEnter the time:\n")

t=input()


if t>"0500" and t<="1159":
    print("Good Morning")
    
if t>"1200" and t<="1659":
    print("Good Afternoon")
    
if t>"1700" and t<="2059":
    print("Good Evening")
    
if (t>"2100" and t<="2400") or  t<="0459":
    print("Good Night")