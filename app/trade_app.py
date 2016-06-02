# -*- coding: utf-8 -*-
from .match.match import OrderMatch
from . import celery
from flask import current_app

@celery.task
def handle_order(order_type, order):
    order_match = OrderMatch()
    if order_type == 'cancel':
        order_match.cancel(order)
    else:
        order_match.submit(order)
    dealed_order = order_match.deal()
    current_app.logger.warning(dealed_order)
