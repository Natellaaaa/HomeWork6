# Задание 1

class Soda:
    def __init__(self, supplement):
        self.supplement = supplement
    
    def show_my_drink(self):
        if self.supplement:
            return f"Газировка и {self.supplement}"
        else:
            return f"Обычная газировка"

my_soda = Soda("лимон")
print(my_soda.show_my_drink())
another_soda = Soda(None)
print(another_soda.show_my_drink())

# Задание 2

import random

class Exchange:
    def __init__(self, name, currency):
        self.name = name
        self.currency = currency
        self.__balance = 0
    
    def make_money(self):
        earned_money = random.randint(100, 1000)
        self.__balance += earned_money
        return f"Вы заработали: {earned_money} KGS"
    
    def to_dollar(self):
        dollar_amount = self.__balance
        self.__balance = dollar_amount * 0.011397
        self.currency = "USD"
        return f"Обмен на доллары: {self.__balance:.2f} долларов"

    def to_euro(self):
        euro_amount = self.__balance
        self.__balance = euro_amount * 0.010469
        self.currency = "EUR"
        return f"Обмен на евро: {self.__balance:.2f} евро"

    def to_ruble(self):
        ruble_amount = self.__balance
        self.__balance = ruble_amount * 1.04
        self.currency = "RUB"
        return f"Обмен на рубли: {self.__balance:.2f} рублей"

    def info(self):
        return f"Имя:||{self.name}|| Баланс:||{self.__balance:.2f}|| Валюта:||{self.currency}||"

exchange = Exchange("Роберт", "KGS")

print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣦⣄⠀⠀⠛⢿⣿⣿⡿⠛⠀⠀⣠⣴⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣤⡀⠀⢹⡏⠀⢀⣤⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⠀⠛⢿⣿⣦⣼⡇⠀⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣦⣀⠀⠉⠻⢿⣧⣴⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠹⣿⣿⣶⣄⠀⢸⣿⣿⣿⣿⣿⣿⠏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢷⣆⡀⠀⠙⠿⣿⠀⢸⡿⠋⣿⠿⠋⠀⢀⣰⡾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠉⠻⣦⣀⠀⠁⠀⢸⡇⠀⠈⠀⣀⣴⠟⠉⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠙⠿⣤⡀⢸⡇⢀⣤⠿⠋⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠈⠻⣿⣿⠟⠁⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print(exchange.info())
print(exchange.make_money())
print(exchange.info())

print(exchange.to_dollar())
print(exchange.info())

# print(exchange.to_euro())
# print(exchange.info())

# print(exchange.to_ruble())
# print(exchange.info())

# Т.к значение у нас возвращается выполнять обмен валют стоит только при отключение обмена других валют
# P.S данные обмена валют были скопированы из сайта Национального Банка Кыргызстана 08.07.2023 в 00:20
# Обмен валют в другие дни могут быть НЕТОЧНЫМИ!