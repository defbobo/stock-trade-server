# -*- coding: utf-8 -*-
from utils import BaseQueue, OrderQueue
from flask import current_app

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
        current_app.logger.warning(max_buy)
        current_app.logger.warning(min_sell)

        max_buy_price, max_buy_order = (max_buy if max_buy else (0, None))
        min_sell_price, min_sell_order = (min_sell if min_sell else (0, None))

        deal_list_pool = []
        if not max_buy_price * min_sell_price:
            return False, deal_list_pool

        current_app.logger.warning('debug identify')

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
