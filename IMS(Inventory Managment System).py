print("\nWellcome to inventory managment system\n(Powerd by FE-Group02-UOC)\n")

product={}                                                                                                                                                          ##This is our main inventory
product_Id=0
productId_list=[]                                                                                                                                                    #To get all th eproduct ID's inveontory have
response=0



while response!="9":                                                                                                                                                 ##Until hit 9(exit), program runs

    response = input("\nPlease enter,\n1 to add new product\n2 to add quantity to existing product\n3 to search product\n4 to place an order\n9 to exit\n_")
    if response =="1":                                                                                                                                               ##Add product to the inventory

        def product_details():                                                                                                                                       ##function that contain product details
            global product_Id
            product_name=input("Enter product name\n:")
            if len(product_name)>0:
                quantity=input("How much quantity have\n:")
                if quantity.isdigit():                                                                                                                                   #cheching user input is a number or not
                        quantity = int(quantity)
                        unit_price = input("Enter price of a unit($)\n:")
                        try:                                                                                                                      #cheching user input is a number or not
                            unit_price = float(unit_price)
                            product_Id =product_Id + 1                                                                                                                      ##This will create unique ID for products
                            productId_list.append(product_Id)                                                                                                               #Add the product ID to the list

                            product[product_Id] = {"Product name": product_name, "Quantity": quantity,"Unit price($)": unit_price}                                          #adding new product to the inventory
                            print("You added the product-",product[product_Id])

                        except ValueError:
                            print("\n**product insert failed**\nInvalid Input.Enter a number\n")

                else:
                    print("\n**product insert failed**\nInvalid Input.Enter a whole number")
            else:
                print("\n**product insert failed**\nName cannot be empty\n")


        product_details()



    if response=="2":                                                                                                                                                ##cahnge the product quantity in inventory
        print("select the product you want to change quantity\n\n")
        for key,values in product.items():
            print(f"{key}:{values}")
        selection=int(input("Product ID\n:"))                                                                                                                       ##to get user response(ehat product quantty should change)
        for x in productId_list:                                                                                                                                    #exception handling(If user enter wronge product ID)
            if x==selection:
                    product[selection]["Quantity"]=input("Enter the new quantity:")
                    print("\nThis is the updated product\n")
                    print(product[selection],"\n")
                    break
        else:
            print("\nproduct ID that you entered is invalid\n")



    if response=="3":                                                                                                                                               #to show product that user wants
        resp=input("\nenter 1 to search product by ID\nenter 2 to view full inventory\n")                                                                           #get user input
        if resp=="1":
            search_1=int(input("Enter product ID:\n"))                                                                                                              # get product that user want
            for x in productId_list:                                                                                                                                 #exception handling(If user enter wronge product ID)
                if x==search_1:
                    print(product[search_1])
                    break
            else:
                print("\nproduct ID you entered doesn't exist\n")

        elif resp=="2":
            for key,value in product.items():
                print(f"{key}:{value}")

        else:
            print("\nInvalid Input\n")


    if response=="4":                                                                                                                                                #Order placing portal

        cart={}                                                                                                                                                     ##this dictionary use to cllect orders. order ID as key & quantity as value
        print("\nTo place an order, please select product ID you want\n")
        for key,value in product.items():                                                                                                                           #print the inventory
            print(f"{key}:{value}")
        order = int
        countorder=0
        Total_cost = {}                                                                                                                                              #checkout amount

        while order!=0:                                                                                                                                             #This will give ability to add multiple orders

            countorder=countorder+1                                                                                                                                  ##to track how many sub orders are there
            print("\nsub-order",countorder)
            order_product = int(input("enter product ID_"))                                                                                                                  #to get user response ehat user want to order

            for f in productId_list:                                                                                                                                #This is for check that product ID that entered by user is available or not
                if f==order_product:
                    order_qnt=int(input("Enter quantity you want:"))                                                                                                #to get order quantity from user
                    if order_qnt<=int(product[order_product]["Quantity"]):                                                                                          #To check quantity that user need is avilable in the inventory
                        if order_product not in cart:
                            cart[order_product]={"Product Id":order_product,"Quantity":order_qnt,"Total sub-cost":order_qnt*product[order_product]["Unit price($)"]}    #this will create "order_product" key & order_qnt value in the cart dictionary
                            product[order_product]["Quantity"] -= order_qnt                                                                                             #This will update the inventory quantity
                            Total_cost[order_product]=cart[order_product]["Total sub-cost"]                                                                             #adding each sub cost to checkout balance
                            order = int(input("\n***Order added to the cart***\nEnter 1 To place an another order or change previos order quantity)\n(To change quantity of previos order, enter product ID you want & enter amount as (-) to deduct)\n\nTo checkout press 0\n_"))

                        else:
                            cart[order_product]["Quantity"] = cart[order_product]["Quantity"] + order_qnt                                                                      #update existing order quantity
                            cart[order_product]["Total sub-cost"] = cart[order_product]["Quantity"] * product[order_product]["Unit price($)"]                                      #updatting sub-cost
                            product[order_product]["Quantity"] =product[order_product]["Quantity"]- order_qnt                                                                                              # This will update the inventory quantity
                            Total_cost[order_product] = cart[order_product]["Total sub-cost"]                                                                       #update total cost after sub-cost got chnged
                            order = int(input(
                                "\n***Order added to the cart***\nEnter 1 To place an another order or change previos order quantity)\n(To change quantity of previos order, enter product ID you want & enter amount as (-) to deduct)\n\nTo checkout press 0\n_"))
                    else:                                                                                                                                            #exception handling(If not enough quantity in the inventory)
                        print("\nOrder quantity is out of range,Enter quantity range within stock")
                        print("Available quantity is:",product[order_product]["Quantity"])
                        order = int(input("\nTo place an order again,enter 1\nTo checkout press 0\n"))
                        countorder = countorder - 1                                                                                                                    #Reset the order count
                        break
                else:
                    print("\nOrder ID you entered is not available\n")
                    countorder = countorder - 1                                                                                                                            #Reset the order count

        print("\nThis is the order you placed\n")                                                                                                                       ##to show what user aded to the cart


        for key,value in cart.items():                                                                                                                                   #print sub-orders
            print(f": {value}")


        print("\nThis is your Total cost-$",sum(Total_cost.values()))                                                                                                            ##calculate total cost
        print("\n  ***\nThank you\n  ****")


else:
        print("**Bye**\nSee you again\nThank you for using Inventory Managment System\n(Powerd by FE-Group02-UOC)\n ")

        