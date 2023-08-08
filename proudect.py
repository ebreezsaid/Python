class Prouduct():
    def __init__(self,name,category,price):
        self.name = name
        self.category = category
        self.price = price
        
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
    def get_price(self):
        return self.price

    def set_name(self,newName):
        self.name = newName
  
    
    
    def descrip(self):
        return f"prouduct:{self.name},category:{self.category}, price:{self.price}"
    
    def discont(self,amount):
        self.price = self.price - (self.price * amount/100)
        if self.category == "Electronics":
            self.price += 10
            
            
            
    