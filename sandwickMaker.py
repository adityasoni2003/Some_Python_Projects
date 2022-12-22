import pyinputplus as pyip                    


your_bill = []
prices = {"Wheat":22,"White":20,"Sourdough":25,"Cheddar":10,"Swizz":12,"Mozzarella":15}

no_of_sandwiches = pyip.inputInt("How many sandwiches do you want",min=1)


response = pyip.inputMenu(['Wheat','White','Sourdough'],"What Type of bread do you want\n", numbered=True)
if response in prices :
    your_bill.append(prices[response])

wanna_cheese = pyip.inputYesNo("Do you want Cheese ?")
if wanna_cheese.lower() == "yes":
    cheese_type = pyip.inputMenu(['Cheddar','Swizz','Mozzarella'],"What type of cheese do you want ?\n")
    if cheese_type in prices:
        your_bill.append(prices[cheese_type])
toppings = pyip.inputYesNo("Do you want toppings ?")
if toppings.lower() == "yes":
    your_bill.append(10)
    
total_Bill = sum(your_bill) *no_of_sandwiches
print("Your Total bill : ",total_Bill)
    
    