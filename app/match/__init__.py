from . import utils, order, match
from ..models import Order, Stock, CancelOrder
from .. import celery

class TradeApplication(object):

    def __init__(self):
        self.om = match.OrderMatch()

    def log(self):
        pass

    def run(self):
        new_orders = self.db_session.query(Order).order_by(Order.submit_time)
        for order in new_orders:
            self.om.submit(order)

        cancel_orders = self.db_session.query(CancelOrder)
        for cancel_order in cancel_orders:
            self.om.cancel(cancel_orders)

@celery.task
def match(order):
    order_match = match.OrderMatch()
    if order['type'] in ['buy', 'sell']:
        order_match.submit(order)
        dealed_list = order_match.deal()
    else:
        order_match.cancel(order)
    if dealed_list:
        for order in dealed_list:
            dealed_order = DealedOrder(order)
            db.session.add(dealed_order)
        db.commit()



