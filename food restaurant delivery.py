# food restaurant delivery
order ={
"client": "John Doe",
"item": "Salad",
"quantity":8,
"price":15.00
}
order["total"]=order["price"]*order["quantity"]


if order["quantity"]>7:
    order["price"]*=0.8 #offer 20% discount for orders from 8 pcs
    order["total"]=order["price"]*order["quantity"]
    print ("\nYou've got 20% discount")

delivery_request =  input("\nDo you need delivery? Yes/No : ")
if delivery_request=="Yes" and order["total"]>300:
    print(f"\nYou've got free delivery. You have to pay {order['total']}")
elif delivery_request=="Yes":
    order["delivery_cost"]=50
    print (f'''You have to pay: \n{order["item"]:10}:{order["total"]:9} 
Delivery  : {order["delivery_cost"]:8.1f}
Total     : {order["total"]+order["delivery_cost"]:8}''', sep="")
else:
    print(f"""\nYou have to pick up the order yourself.
You have to pay {order['total']}
""")
