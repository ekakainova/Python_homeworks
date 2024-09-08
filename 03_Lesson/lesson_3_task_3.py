from address import Address
from mailing import Mailing

address1 = Address(123456, "Москва", "Молостовых", 21, 125)
address2 = Address(123456, "Санкт-Петербург", "Маршала Говорова", 37, 36)

print(Mailing(address1, address2, 600, 235478669))
