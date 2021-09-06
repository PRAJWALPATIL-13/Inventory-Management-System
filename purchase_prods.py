import json

with open("IMSrecord.json",'r') as fl:
    r = fl.read()

records = json.loads(r)

i_prod  = input("Enter the product Id: ")
i_quant = int(input("Enter the product Quantity: "))
print('*'*24)
print("Product: ", records[i_prod]['Name'])
print("Cost: ", records[i_prod]['Cost'])
print("Category:",records[i_prod]['Category'])
print("Location:",records[i_prod]['Location'])
print('-'*24)
print("Billing Amount: ", records[i_prod]['Cost'] * i_quant)
print('*'*24)

records[i_prod]['Quantity'] = records[i_prod]['Quantity'] - i_quant

js = json.dumps(records)

with open("IMSrecord.json",'w') as fs:
    fs.write(js)