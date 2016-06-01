# -*- coding: utf-8 -*-

from collections import OrderedDict

class BaseQueue1(object):
    """Base queue like strcture"""

    def __init__(self):
        self._queue = OrderedDict()

    def __getitem__(self, key):
        return self._queue[key]

    def __setitem__(self, key, value):
        self._queue[key] = value

    def insert(self, key, value):
        self._queue[key] = value

    def get(self, key):
        return self._queue.get(key)

    def remove(self, index):
        del self._queue[index]

    def pop_min(self):
        if self._queue:
            min_value, min_key = min(zip(self._queue.values(),
                                         self._queue.keys()))
            return (min_key, self._queue.pop(min_key))

    def pop_max(self):
        if self._queue:
            max_value, max_key = max(zip(self._queue.values(),
                                         self._queue.keys()))
            return (max_key, self._queue.pop(max_key))

    def min_item(self):
        if self._queue:
            min_key, min_value = min(zip(self._queue.keys(),
                                         self._queue.values()))
            return min_key, min_value

    def max_item(self):
        if self._queue:
            max_key, max_value = max(zip(self._queue.keys(),
                                         self._queue.values()))
            return max_key, max_value

    @property
    def count(self):
        return len(self._queue)


class BaseQueue2(OrderedDict):
    """Queue like hash type class"""

    def insert(self, key, value):
        self[key] = value

    def remove(self, key):
        del self[key]

    @property
    def count(self):
        return len(self)

    def min_item(self):
        if self.count:
            min_key, min_value = min(zip(self.keys(), self.values()))
            return min_key, min_value

    def max_item(self):
        if self.count:
            max_key, max_value = max(zip(self.keys(), self.values()))
            return max_key, max_value

    def pop_min(self):
        if self.count:
            min_key, min_value = min(zip(self.keys(), self.values()))
            return self.pop(min_key)

    def pop_max(self):
        if self.count:
            max_key, max_value = max(zip(self.keys(), self.values()))
            return self.pop(max_key)


class OrderQueue(object):
    """Order Queue"""

    def __init__(self):
        self._queue = BaseQueue()
        self.totalAmount = 0.0

    def __setitem__(self, key, value):
        self._queue[key] = value

    def __getitem__(self, index):
        return list(self._queue.values())[index]

    def __repr__(self):
        return 'Order queue({!r})'.format(self._queue)

    def append(self, order):
        index = order.timestamp
        self._queue.insert(index, order)
        self.totalAmount += self._queue[index].amount

    def count(self):
        return self._queue.count

    def min_item(self):
        return self._queue.min_item()

    def eat(self, amount):
        current_amount = amount
        to_pop_orders = []
        while self.totalAmount > 0 and current_amount > 0:
            if not self._queue or self._queue.count == 0:
                self.totalAmount = 0.0
                return []

            _, min_item = self._queue.min_item()
            min_i = min_item
            if min_i.amount <= current_amount:
                current_amount -= min_i.amount
                self.totalAmount -= min_i.amount
                to_pop_orders.append(self._queue.pop_min())
                continue

            elif min_i.amount > current_amount:
                new_order = min_i.copy_order()
                new_order.amount = current_amount
                to_pop_orders.append(new_order)
                min_i.amount -= current_amount
                self.totalAmount -= current_amount
                current_amount = 0
                break
        return to_pop_orders

    def remove(self, order):
        index = order.timestamp
        self.totalAmount -= self._queue[index].amount
        return self._queue.remove(index)

    def get_price_depth(self):
        return self.totalAmount

    def is_empty(self):
        return self._queue.count == 0

BaseQueue = BaseQueue2
