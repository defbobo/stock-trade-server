# -*- coding: utf-8 -*-
import unittest

from app.models.utils import BaseQueue, OrderQueue

class TestQueue(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_string(self):
        bq = BaseQueue()
        bq['abc'] = 10
        self.assertEqual(bq.get('abc'), 10)


if __name__ == '__main__':
    unittest.main()
