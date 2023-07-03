class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phoneNumber):
        print(f"{self.brand} is calling {phoneNumber}")

    def __str__(self):
        return f"Brand = {self.brand}\nPrice = {self.price}"


iphone = Phone("iPhone 14", 1000)
galaxy = Phone("Galaxy S23", 700)


def print_hi(name):
    print(f'Hi, {name}')
    print(iphone.brand)
    print(iphone.price)


if __name__ == '__main__':
    print_hi('PyCharm')
