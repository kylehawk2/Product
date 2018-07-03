class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price 
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, tax):
        self.price += tax
        return self
    def item_return(self, reason, tax):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'brand new':
            self.status = 'for sale'
            self.price -= tax
        else:
            self.status = 'used'
            self.price -= tax
            self.price = self.price - (self.price * .2)
        return self
    def display_info(self):
        print 'Name: ' + self.name + ' | Brand: ' + self.brand + ' | Status: ' + self.status + ' | Weight: ' + str(self.weight) + ' | Price: ' + str(self.price)
        return self

gpu = Product(1600, 'gpu', 5, 'Nvidia')
gpu.add_tax(.1).sell().item_return('Brand New', .1).display_info()