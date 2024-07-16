class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is str and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
        
    
    def customers(self):
        return list(set(order.customer for order in self.orders()))
        pass
    
    def num_orders(self):
        return len(self.orders())
        pass
    
    def average_price(self):
        prices = [order.price for order in Order.all if order.coffee == self]
        return sum(prices) / len(self.orders())

class Customer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is str and 1 < len(name) < 15:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
        
    
    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    
    def create_order(self, coffee, price):
        custom_order = Order(self, coffee, price)
        return custom_order
        
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if type(price) is float and 1.0 < price < 10.0 and not hasattr(self, "price"):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee