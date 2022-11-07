products = {
				  "Apple":  20,
				  "Banana": 15,
				  "Cherry": 10,
				}
ProductsQuantity = {
	              "Apple": 40,
				  "Banana": 30,
				  "Cherry": 70,
	            }
AddedProduct = 0
print("\t\t\t\t\tWelcome to ITI Shop")
print("\t\t\t\t\t********************")
while True:
	x = input("Select Mode For customer press 1, for owner press two, to exist press 0: ")
	x = int(x)
	if x == 1:   #Customer
			print("Hello Customer....")
			while True:
				customer=input("To show our products press 1, To buy from our products press 2, To print the bill press 3, To exit press 0: ")
				customer=int(customer)
				if customer == 1:
					print("Available Number of each Product: ",ProductsQuantity)
					print("Cost of each Product",products)
					print("--------------------------------------------"*2)
				elif customer == 2:
						sum=0
						while True:
							select = input("Please select the product you want: ")
							select = int(select)
							if select == 1:  
								sum = sum+products["Apple"]	
							elif select == 2:  
								sum = sum+products["Banana"]
							elif select == 3:  
								sum = sum+products["Cherry"]
							elif select == 4:
							    sum=sum+AddedProduct
							else:
								print("Exit")
								print("--------------------------------------------"*2)
								break;				   
				elif customer == 3:
					print("The bill = ",sum)
					print("--------------------------------------------"*2)
				elif customer == 0:
					print("Exit")
					break;
	elif x == 2:   #ITI Owner
			while True:
				owner = input("Add products press 1, show products press 1,Add cost press 1,change cost press 2, To exit press 3: ")
				owner = int(owner)
				if owner == 1:
					while True:
						ProductSelect = input("The owner select: ")
						ProductSelect = int(ProductSelect)
						if ProductSelect == 1:
							key = input("Add products: ")
							salaryitem = input("Add salary of product: ")
							salaryitem = int(salaryitem)
							NoOfAvailable = input("Number of the product: ")
							NoOfAvailable = int(NoOfAvailable)
							products[key] = salaryitem
							AddedProduct = salaryitem
							ProductsQuantity[key] = NoOfAvailable
							print("Available Number of each Product: ",ProductsQuantity)
							print("Cost of each Product: ",products)
							print("--------------------------------------------"*2)
						elif ProductSelect == 2:
							print("--------------------------------------------"*2)
						break;	
				elif owner == 2:
						ChangeCost = input("Change Cost: ")
						ChangeCost = int(ChangeCost)
						key = input("Select Product: ")
						products[key] = ChangeCost
						AddedProduct = ChangeCost
						print("Cost of each Product: ",products)
						print("--------------------------------------------"*2)						
				elif owner == 3:
						print("Exit")
						print("--------------------------------------------"*2)
						break;
	elif x == 0:
			print("Exit")
			print("--------------------------------------------"*2)
			break;
			
    
        
