userName = 0
passWord = 0
while userName != "Palm" or passWord != "2012":
    userName = input("USERNAME : ")
    passWord = input("PASSWORD : ")
    if userName != "Palm" and passWord != "2012":
            print("USERNAME and PASSWORD was wrong try again ")
    elif userName !="Palm" and passWord == "2012":
            print("USERNAME was wrong try again")
    elif userName =="Palm" and passWord != "2012":
            print("PASSWORD was wrong try again")
    else :
            print("SUCCESS")
print("--- WELCOME ITEM SHOP DOTA2 ---")
print("WHAT DO YOU WANT ITEM?")
print("1.Sentry Ward : 50 Gold")
print("2.Blood Grenade : 65 Gold")
print("3.Bottle : 675 Gold")
print("4.Aghanim's Shard : 1,400 Gold")
print("5.Blink Dagger : 2,250 Gold")
userSelect = 0
while userSelect != range(5):
    userSelect = int(input("You want item number :"))
    if userSelect == 1:
        x = int(input("How many : "))
        price = 50
        result = x * price
        print("Total :",result,"Gold")
    elif userSelect == 2:
        x = int(input("How many :"))
        price = 65
        result = x * price
        print("Total :",result,"Gold")
    elif userSelect == 3:
        x = int(input("How many :"))
        price = 675
        result = x * price
        print("Total :",result,"Gold")
    elif userSelect == 4:
        x = int(input("How many :"))
        price = 1400
        result = x * price
        print("Total :",result,"Gold")
    elif userSelect == 5:
        x = int(input("How many :"))
        price = 2250
        result = x * price
        print("Total :",result,"Gold")
    else :
        print("Try again !!!")
print("--- THANK YOU ---")