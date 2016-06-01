# -*- coding: utf-8 -*-

class Order(object):
    """Stock Order data model"""

    def __init__(self, id, timestamp, symbol, type, price, amount):
        self.id = id
        self.timestamp = timestamp
        self.symbol = symbol
        self.type = type
        self.price = price
        self.amount = amount

    def __repr__(self):
        return ('Stock_order: {!r}, price: {!r}, amount: {!r}'
                .format(self.symbol, self.price, self.amount))

    def __gt__(self, other):
        if self.price < other.price:
            return False
        elif self.price == other.price:
            if self.timestamp <= other.timestamp:
                return False
            else:
                return True
        else:
            return True

    def __ge__(self, other):
        if self.price > other.price:
            return False
        elif self.price == other.price:
            if self.timestamp > other.timestamp:
                return False
            else:
                return True
        else:
            return True

    def copy_order(self):
        copy_order = Order(self.id, self.timestamp, self.symbol, self.type,
                           self.price, self.amount)
        return copy_order
