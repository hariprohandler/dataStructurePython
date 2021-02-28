expenditure = {}
with open("price.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        expenditure[tokens[0]] = float(tokens[1])
print(expenditure)
for element in expenditure:
    print(element)
        