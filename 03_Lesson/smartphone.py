class Smartphone:

    def __init__(self, brand, phoneModel, number):
        self.brand = brand
        self.phoneModel = phoneModel
        self.number = number

    def __str__(self):
        return f"{self.brand} - {self.phoneModel}. {self.number}"
