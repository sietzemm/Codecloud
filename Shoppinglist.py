import sys

global list_size
global list_name
global main_list
global item_price_total
global list_prices
global totalPrice

list_prices = []
list_name = []

def CreateList():

    list_name = input("Please enter the name of your new list : ")
    list_size = input("Please enter the size of your new list : ")

    vars()[list_name] = [] * int(list_size)
    global name_placeholder
    name_placeholder = list_name
    print("Your new list with name : " + list_name + "has been successfully created with size : " + list_size + ".")

    global list_placeholder
    list_placeholder = [] * int(list_size)


def addItem():
    global sharedprice
    print("Please add items to your list : ")
    item_name  = input("Name of item : ")
    item_price = input("Please add a price : ")

    item_price_placeholder = float(item_price)
    list_prices.append(item_price_placeholder)

    tup = item_name, item_price
    list_placeholder.append(tup)

    conditional = input("Do you want to add more items to your list ? type Y/N.")

    if conditional == "Y":
        addItem()
    else :
        print("Your list has been created.")
        totalPrice = sum(list_prices)
        sharedprice = totalPrice

def showList(sharedprice):
    t = sharedprice
    # calculate total items in list
    length_list = (len(list_placeholder))
    print(type(list_prices))

    print("##############")
    print(list_placeholder)
    print("##############")
    print("Total amount of items in list : " + str(length_list) + ".")
    print("Total price of items in the list : " + str(t) + ".")
    print("##############")
    
CreateList()
addItem()
showList(sharedprice)
