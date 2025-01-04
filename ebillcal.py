
exit='a'
print("Electricity bill calculator\n")
cost=[]
while exit!='e':


    unit=int(input("Enter the unit consumed:\n_"))


    if unit<=60:

        if unit<=30:
            cost1=(unit*2.50)+30
            cost.append(cost1)

            tot = sum(cost)
            print("Your final bill is= Rs.", tot,"\n")

            print("This is how your bill was calculated\n")
            print("Fist",unit, "Units-", cost[0], "( Rs.30 Fixed charges added)")
        else:
            cost2=(30*2.50)+60+30
            cost3 = ((unit - 30) * 4.85)
            cost.insert(0,cost2)
            cost.insert(1,cost3)

            tot = sum(cost)
            print("Your final bill is= Rs.", tot,"\n")

            print("This is how your bill was calculated\n")
            print("Fist 30 Units-", cost[0], "( Rs.30 Fixed charges added)")
            print("next",(unit-30),"Units-",cost[1],"(Rs.60 Fixed charges added)")
    else:


        if unit<=90:
            cost2=(60 * 7.85) + 00
            cost3=((unit-60)*10)+90
            cost.insert(0,cost2)
            cost.insert(1,cost3)

            tot = sum(cost)
            print("Your final bill is= Rs.", tot, "\n")

            print("This is how your bill was calculated\n")
            print("First 60 Units-", cost[0], "( Rs.00 Fixed charges added)")
            print("next", (unit - 60), "Units-", cost[1], "( Rs.90 Fixed charges added)")

        elif unit<=120:
            cost4=(60*7.85)
            cost5=(30*10)+90
            cost6=((unit-90)*27.75)+480
            cost.insert(0,cost4)
            cost.insert(1,cost5)
            cost.insert(2,cost6)

            tot = sum(cost)
            print("Your final bill is= Rs.", tot, "\n")

            print("This is how your bill was calculated\n")
            print("First 60 Units-", cost[0], "( Rs.00 Fixed charges added)")
            print("second 30 Units-", cost[1], " (Rs.90 Fixed charges added)")
            print("next", (unit - 90), "Units-", cost[2], "( Rs.480 Fixed charges added)")

        else:
            cost6=(60*7.85)
            cost7=(30*10)+90
            cost8=(30*27.75)+480
            cost9=((unit-120)*32)+480
            cost.insert(0,cost6)
            cost.insert(1,cost7)
            cost.insert(2,cost8)
            cost.insert(3,cost9)

            tot = sum(cost)
            print("Your final bill is= Rs.", tot, "\n")

            print("This is how your bill was calculated\n")
            print("First 60 Units-", cost[0], "( Rs.00 Fixed charges added)")
            print("second 30 Units-", cost[1], "( Rs.90 Fixed charges added)")
            print("next 30 Units-", cost[2], "( Rs.480 Fixed charges added)")
            print("next", (unit - 120), "Units-", cost[3], "( Rs.480 Fixed charges added)")

    exit = input("\nEnter any key to calculate again\nEnter 'e' to exit\n_")
