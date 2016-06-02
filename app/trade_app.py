# -*- coding: utf-8 -*-
from .match.match import OrderMatch
from .match.order import Order
from . import celery
import json

order_match = OrderMatch()

@celery.task
def handle_order(order_type, order):
    # current_app.logger.warning(order)
    order = json.loads(order)
    # current_app.logger.warning(order)
    order_id = order['order_id']
    timestamp = order['submit_time']
    symbol = order['symbol']
    order_type = order['order_type']
    price = order['price']
    amount = order['amount']

    new_order = Order(order_id, timestamp, symbol, order_type, price, amount)
    global order_match

    if order_type == 'cancel':
        order_match.cancel(new_order)
    else:
        order_match.submit(new_order)

    _, dealed_order = order_match.deal()
    return dealed_order
