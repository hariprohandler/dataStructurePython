finalizeOrder =  False
while(finalizeOrder == False):
    processorType = int(input("Enter 8/16/32bit process "))
    orderQuantity = int(input("Enter number of required quantity "))
    typeOfOrg=input(" I -> Individual, G-> Givernment, U-> unitversity ")
    confirm = int(input(f" You are requesting {orderQuantity} quantity for {typeOfOrg} Industry, press 1 to confirm "))
    if(confirm == 1):
        finalizeOrder = True
discountVal = 0
if(processorType == 32):
    if(orderQuantity < 50000):
        if(typeOfOrg == 'I'):
            discountVal = 0.05
        elif(typeOfOrg == 'G'):
            discountVal = 0.065
    elif(orderQuantity >= 50000):
        if(typeOfOrg == 'I'):
            discountVal = 0.075
        elif(typeOfOrg == 'G'):
            discountVal = 0.085
    elif(orderQuantity == 100000):
        if(typeOfOrg == 'I' or typeOfOrg == 'G'):
            discountVal = 0.1
    elif(orderQuantity > 100000):
        discountVal = 0.075
print(f"The discount is {discountVal} ")