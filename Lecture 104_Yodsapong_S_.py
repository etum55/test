class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Yodsapong"
customer1.lastName = "Sujjapongse"
customer1.age = 23
customer1.addCart()
customer2 = Customer()
customer2.name = "Yodsapong2"
customer2.lastName = "Sujjapongse2"
customer2.age = 24
customer2.addCart()