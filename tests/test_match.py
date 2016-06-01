# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import unittest

from datetime import datetime

from app.models.match import OrderMatch
from app.models.order import Order

class TestOrdermatch(unittest.TestCase):

    def setUp(self):
        self.om = OrderMatch()
        self.buy1 = Order('1', datetime.now(), 'aa', 'buy', 91, 100)
        self.buy2 = Order('2', datetime.now(), 'ab', 'buy', 100, 200)
        self.buy3 = Order('3', datetime.now(), 'ac', 'buy', 90, 300)
        self.buy4 = Order('4', datetime.now(), 'ad', 'buy', 95, 400)
        self.sell1 = Order('1', datetime.now(), 'ba', 'sell', 100, 10)
        self.sell2 = Order('2', datetime.now(), 'bb', 'sell', 110, 20)
        self.sell3 = Order('3', datetime.now(), 'bc', 'sell', 105, 30)
        self.sell4 = Order('4', datetime.now(), 'bd', 'sell', 104, 40)

    def tearDown(self):
        pass

    def test_match_init(self):
        self.assertIsInstance(OrderMatch(), OrderMatch)

    def test_submit(self):
        self.assertIsNone(self.om.submit(self.buy1))

    def test_cancel(self):
        self.assertIsNone(self.om.submit(self.buy1))
        self.assertIsNone(self.om.cancel(self.buy1))

    # @unittest.skip('skipped test')
    def test_closest_pair(self):
        self.assertIsNone(self.om.submit(self.buy1))
        self.assertIsNone(self.om.submit(self.buy2))
        self.assertIsNone(self.om.submit(self.buy3))
        self.assertIsNone(self.om.submit(self.buy4))
        self.assertIsNone(self.om.submit(self.sell1))
        self.assertIsNone(self.om.submit(self.sell2))
        self.assertIsNone(self.om.submit(self.sell3))
        self.assertIsNone(self.om.submit(self.sell4))
        max_buy, min_sell = self.om.closest_pair()
        print(max_buy[0], min_sell[0])

    def test_deal(self):
        self.assertIsNone(self.om.submit(self.buy1))
        self.assertIsNone(self.om.submit(self.buy2))
        self.assertIsNone(self.om.submit(self.buy3))
        self.assertIsNone(self.om.submit(self.buy4))
        self.assertIsNone(self.om.submit(self.sell1))
        self.assertIsNone(self.om.submit(self.sell2))
        self.assertIsNone(self.om.submit(self.sell3))
        self.assertIsNone(self.om.submit(self.sell4))
        print(self.om.deal())

if __name__ == '__main__':
    unittest.main()
