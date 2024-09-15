class Product:

    def __init__(self, name, price):
        self.productName = name
        self.productPrice = price

    def NameOfProduct(self):
        return self.productName

    def PriceOfProduct(self):
        return self.productPrice

    def ProductInfo(self):
        return f'Продукт - {self.productName} стоит {self.productPrice} рублей.'
