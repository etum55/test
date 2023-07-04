menuList = []
priceList1 = []

def showBill():
    totalPrice = 0
    print("--- My Food ---")
    for number in range(len(menuList)):
        print(menuList[number],priceList1[number])
        totalPrice += int(priceList1[number])
    print("Totel :", totalPrice)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == ("exit")):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList1.append(menuPrice)
showBill()