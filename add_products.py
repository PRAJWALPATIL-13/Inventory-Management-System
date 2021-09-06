import json
rec={}
ans=True
while (ans):
    prod_id=int(input("Enter the product id:"))
    cat=input("Enter the product category:")
    name=input("Enter the product name:")
    quan=int(input("Enter the product quantity:"))
    loc=input("Enter the product location:")
    cost=int(input("Enter the cost of the product:"))

    rec[prod_id]={'Category':cat,'Name':name,'Quantity':quan,'Location':loc,'Cost':cost}
    js=json.dumps(rec)
    with open('IMSrecord','a+') as fl:
        fl.write(rec[prod_id])

    ans=input("Do you want to continue? y/n: ")
    if ans=='n':
        break
    else:
        continue