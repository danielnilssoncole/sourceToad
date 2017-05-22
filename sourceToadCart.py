# Python 2.7.11

class Customer:
    def __init__(self, first_name, last_name, address_1, address_2, city, state, zip):
        self.first_name = first_name
        self.last_name = last_name
        self.address_1 = address_1
        self.address_2 = address_2
        self.cit = city
        self.state = state
        self.zip = zip

    def print_full_name(self):
        print(self.first_name + ' ' + self.last_name)

    def print_address(self):
        print('{0}{1}{0}{2}{0}{3}, {4} {5}{0}'.format('\n', self.address_1, self.address_2, self.city, self.state, self.zip))

class Item:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.address_1 = customer.address_1
        self.address_2 = customer.address_2
        self.city = customer.city
        self.state = customer.state
        self.zip = customer.zip
        self.contents = []
        self.tax_rate = .07
        self.shipping_rate = .10


    def add_item(self, item):
        if item.id not in [c.id for c in self.contents]:
            self.contents.append(item)

    def remove_item(self, item):
        if item.id in [c.id for c in self.contents]:
            self.contents.remove(item)

    def print_items(self):
        for c in self.contents:
            print(' id: {1}{0} name: {2}{0} quantity: {3}{0} price: {4}{0}'.format('\n', c.id, c.name, c.quantity, c.price))

    def print_address(self):
        print('{0}{1}{0}{2}{0}{3}, {4} {5}{0}'.format('\n', self.address_1, self.address_2, self.city, self.state, self.zip))

    def set_cost(self, item, cost):
        if item.id in [c.id for c in self.contents]:
            item.price = cost

    def show_subtotal(self):
        self.subtotal = 0
        if len(self.contents) > 0:
            for item in self.contents:
                self.subtotal += item.price * item.quantity
            print self.subtotal

    def show_total(self):
        if self.subtotal:
            self.total = self.subtotal * (1 + self.tax_rate + self.shipping_rate)
            print self.total



#requirements from assessment
# Please write two or more classes that allow for the setting and retrieval of the following information:

# - Customer Name
cust1 = Customer('dan', 'none', '7104 Silvermill Dr.', '', 'Tampa', 'FL', 33635)
cust1.first_name = 'Daniel'
cust1.last_name = 'Nilsson-Cole'
cust1.print_full_name()


# - Customer Addresses
cust1.address_1 = '7108 Silvermill Dr.'
cust1.city = 'Miami'
cust1.zip = 33333
cust1.print_address()


# - Items in Cart
cart1 = Cart(cust1)
i1 = Item(2, 'test', 3, 45)
i2 = Item(3, 'test2', 2, 50)
cart1.add_item(i1)
cart1.add_item(i2)
cart1.remove_item(i1)
cart1.print_items()


# - Where Order Ships
cart1.print_address()

# - Cost of item in cart - including shipping and tax
cart1.set_cost(i2, 60)
cart1.print_items()


# - Subtotal and total for all items
cart1.show_subtotal()
cart1.show_total()
