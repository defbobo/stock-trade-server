# -*- coding: utf-8 -*-
import unittest

from datetime import datetime

from app.models.utils import BaseQueue
from app.models.order import Order

class TestBaseQueue(unittest.TestCase):

    def setUp(self):
        self.bq = BaseQueue()
        self.buy1 = Order('1', datetime.now(), 'aa', 'buy', 100, 100)
        self.buy2 = Order('2', datetime.now(), 'ab', 'buy', 110, 200)
        self.buy3 = Order('3', datetime.now(), 'ac', 'buy', 90, 300)
        self.buy4 = Order('4', datetime.now(), 'ad', 'buy', 95, 400)
        self.sell1 = Order('1', datetime.now(), 'ba', 'sell', 100, 10)
        self.sell2 = Order('2', datetime.now(), 'bb', 'sell', 110, 20)
        self.sell3 = Order('3', datetime.now(), 'bc', 'sell', 90, 30)
        self.sell4 = Order('4', datetime.now(), 'bd', 'sell', 95, 40)

    def tearDown(self):
        pass

    def test_insert(self):
        b1 = self.buy1
        s1 = self.sell1
        self.assertIsNone(self.bq.insert(b1.price, b1))
        self.assertIsNone(self.bq.insert(s1.price, s1))

    def test_remove(self):
        b1 = self.buy1
        b2 = self.buy2
        self.bq.insert(b1.price, b1)
        self.bq.insert(b2.price, b2)
        self.assertIsNone(self.bq.remove(b1.price))
        self.assertIsNone(self.bq.remove(b2.price))

    def test_count(self):
        b1 = self.buy1
        b2 = self.buy2
        self.bq.insert(b1.price, b1)
        self.bq.insert(b2.price, b2)
        self.assertEqual(self.bq.count, 2)

    def test_min_item(self):
        b1 = self.buy1
        b2 = self.buy2
        self.bq.insert(b1.price, b1)
        self.bq.insert(b2.price, b2)
        self.assertEqual(self.bq.min_item(), b1)

if __name__ == '__main__':
    unittest.main()
