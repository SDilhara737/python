print("\nWellcome to inventory managment system\n(Powerd by FE-Group02-UOC)\n")

product={}                                                                  ##This is our main inventory
product_Id=0
product_track=[]                                                            ##this shows the all product ID's
response=0

while response!="9":                                                          ##Until hit 9(exit), program runs

    response = input("\nPlease enter,\n1 to add new product\n2 to add quantity to existing product\n3 to search product\n4 to place an order\n9 to exit\n_")
    if response =="1":                                                        ##Add product to the inventory
        product_Id=product_Id+1                                             ##This will create unique ID for products
        def product_details():                                              ##function that contain product details
            product_name=input("Enter product name\n:")
            quantity=input("How much quantity have\n:")

            if quantity.isdigit():                                          #cheching user input is a number or not
                    quantity = int(quantity)
                    unit_price = input("Enter price of a unit($)\n:")
                    if unit_price.isdigit():                                #cheching user input is a number or not
                        unit_price = float(unit_price)

                        product[product_Id] = {"Product name": product_name, "Quantity": quantity,"Unit price($)": unit_price}
                        print("You added the product-",product[product_Id])

                    else:
                        print("Enter a number")
            else:
                print("Enter a whole number")

        product_details()
        product_track.append(product_Id)                                    ##add product ID to the list


    if response=="2":                                                         ##cahnge the product quantity in inventory
        print("select the product you want to change quantity\n\n")
        for key,values in product.items():
            print(f"{key}:{values}")
        selection=int(input("Product ID\n:"))                               ##to get user response(ehat product quantty should change)
        for x in product_track:                                             #exception handling(If user enter wronge product ID)
            if x==selection:
                    product[selection]["Quantity"]=input("Enter the new quantity:")
                    print("\nThis is the updated product\n")
                    print(product[selection],"\n")
                    break
        else:
            print("product ID that you entered is invalid\n")



    if response=="3":                                                         #to show product that user wants
        resp=input("enter 1 to search product by ID\nenter 2 to view full inventory\n") #get user input
        if resp=="1":
            search_1=int(input("Enter product ID:\n"))                          # get product that user want
            for x in product_track:                                             #exception handling(If user enter wronge product ID)
                if x==search_1:
                    print(product[search_1])
                    break
            else:
                print("product ID you entered doesn't exist")

        elif resp=="2":
            for key,value in product.items():
                print(f"{key}:{value}")

        else:
            print("Wronge input")


    if response=="4":                                                         #Order placing portal

        cart={}                                                             ##this dictionary use to cllect orders. order ID as key & quantity as value
        print("\nTo place an order, please select product ID you want\n")
        for key,value in product.items():                                   #print the inventory
            print(f"{key}:{value}")
        order = int
        countorder=0
        Total_cost = []                                                     #checkout amount

        while order!=0:                                                     #This will give ability to add multiple orders

            countorder=countorder+1                                         ##to track how many sub orders are there
            print("sub-order",countorder)
            order_product = int(input("enter product ID_"))                 #to get user response ehat user want to order
            order_qnt=int(input("Enter quantity you want:"))                #to get order quantity from user
            if order_qnt<=int(product[order_product]["Quantity"]):               #To check quantity that user need is avilable in the inventory
                cart[order_product]={"Product Id":order_product,"Quantity":order_qnt,"Total sub-cost":order_qnt*product[order_product]["Unit price($)"]}   #this will create "order_product" key & order_qnt value in the cart dictionary
                product[order_product]["Quantity"] -= order_qnt             #This will update the inventory quantity
                order=int(input("\nOrder added to the cart, To place an another order enter 1\nTo checkout press 0\n"))
                Total_cost.append(cart[order_product]["Total sub-cost"])    #adding each sub cost to checkout balance

            else:                                                           #exception handling(If not enough quantity in the inventory)
                print("\nOrder quantity is out of range,Enter quantity range within stock")
                print("Available quantity is:",product[order_product]["Quantity"])
                countorder=countorder-1                                     #reset order count
                order = int(input("\nTo place an order again,enter 1\nTo checkout press 0\n"))


        print("\nThis is the order you placed\n")                           ##to show what user aded to the cart


        for key,value in cart.items():                                      #print sub-orders
            print(f": {value}")


        print("\nThis is your Total cost-$",sum(Total_cost))                  ##calculate total cost
        print("\n  ***\nThank you\n  ****")


else:
        print("Bye.See you again")

        