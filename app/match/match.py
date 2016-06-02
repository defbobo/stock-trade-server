# -*- coding: utf-8 -*-
from utils import BaseQueue, OrderQueue

class OrderMatch(object):

    def __init__(self):
        self.dealpair = {'buy': BaseQueue(), 'sell': BaseQueue()}

    def submit(self, order):
        order_type = order.order_type
        order_price = order.price
        if not self.dealpair[order_type].get(order_price):
            self.dealpair[order_type].insert(order_price, OrderQueue())
            self.dealpair[order_type][order_price].append(order)
        else:
            self.dealpair[order_type][order_price].append(order)

    def cancel(self, order):
        order_type = order.order_type
        order_price = order.price
        if self.dealpair[order_type].get(order_price):
            self.dealpair[order_type][order_price].remove(order)
            if self.dealpair[order_type][order_price].is_empty():
                self.dealpair[order_type].remove(order_price)
        else:
            pass

    def closest_pair(self):
        return (self.dealpair['buy'].max_item(),
                self.dealpair['sell'].min_item())

    def deal(self):
        max_buy, min_sell = self.closest_pair()
        max_buy_price, max_buy_order = (max_buy if max_buy else (0, None))
        min_sell_price, min_sell_order = (min_sell if min_sell else (0, None))
        # print(max_buy, min_sell)
        deal_list_pool = []

        # print(min_sell[0] <= max_buy[0])

        if min_sell_price <= max_buy_price:
            sell_amount = min_sell_order.get_price_depth()
            buy_amount = max_buy_order.get_price_depth()
            print(sell_amount, buy_amount)

            if sell_amount >= buy_amount:
                sell_bills = min_sell_order.eat(buy_amount)
                buy_bills = max_buy_order.eat(buy_amount)
                deal_list_pool.append([sell_bills, buy_bills])
                # print(deal_list_pool)
            else:
                sell_bills = min_sell_order.eat(sell_amount)
                buy_bills = max_buy_order.eat(sell_amount)
                deal_list_pool.append([sell_bills, buy_bills])
        else:
            return False, deal_list_pool

        if self.dealpair['sell'][min_sell_price]:
            if (self.dealpair['sell'][min_sell_price].is_empty() or
                    min_sell_order.get_price_depth() == 0.0):
                if min_sell_order.get_price_depth() != 0.0:
                    print("error:%.2f\n" % min_sell)
                self.dealpair['sell'].remove(min_sell_price)

        if self.dealpair['buy'][max_buy_price]:
            if (self.dealpair['buy'][max_buy_price].is_empty() or
                    max_buy_order.get_price_depth() == 0.0):
                if max_buy_order.get_price_depth() != 0.0:
                    print("error:%.2f\n" % max_buy)
                self.dealpair['buy'].remove(max_buy_price)

        return True, deal_list_pool

if __name__ == '__main__':
    from order import Order
    from datetime import datetime

    buy1 = Order('1', datetime.now(), 'ab', 'buy', 100, 400)
    buy2 = Order('2', datetime.utcnow(), 'ab', 'buy', 100, 400)
    sell1 = Order('1', datetime.now(), 'bb', 'sell', 100, 200)
    sell2 = Order('2', datetime.utcnow(), 'bb', 'sell', 100, 20)

    om = OrderMatch()
    om.submit(buy1)
    om.submit(buy2)
    om.submit(sell1)
    om.submit(sell2)
    # print(om.closest_pair())
    a, b = om.deal()
    print(b)
