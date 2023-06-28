def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "Palm"and password == "2012":
        return showMenu()
    else:
        return login()
def showMenu():
    print("--- SHOP ---")
    print("1.Vat Calculator")
    print("2.Price Calculator")
    return menuSelect()
def menuSelect():
    userSelected = int(input(">> : "))
    if userSelected == 1 :
        return vatCalculate()
    elif userSelected == 2:
        return priceCalculate()
    elif userSelected != 1 or userSelected != 2:
        return showMenu()
def vatCalculate():
    totalPrice = int(input("TotalPrice : "))
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("Price1 (THB) : "))
    price2 = int(input("Price2 (THB) : "))
    return (price1 + price2)

print(login())
