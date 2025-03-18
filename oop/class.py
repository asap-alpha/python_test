
class Sales:
    def __init__(self, product:str, total:int):
        self.product = product
        self.total = total

sale = Sales("Tomatoes", 20)
print(sale.product)