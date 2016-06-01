# -*- coding: utf-8 -*-

from flask import request, jsonify, abort, current_app
from datetime import datetime
from . import apis
from .redis_queue import send_orders_via_queue
from .. import db, redis
from ..models import Order, Stock, CancelOrder
from ..decorators import accept
from random import randrange


@apis.route("/", methods=['GET'])
def index():
    return 'Hi, welcome XIXI trading center'


@apis.route("/trade.do", methods=['POST'])
@accept('application/json')
def new_trade():
    symbol = request.json.get('symbol')
    order_type = request.json.get('order_type')
    price = request.json.get('price')
    amount = request.json.get('amount')
    order_id = gen_order_id()
    submit_time = datetime.now()

    stock_query = Stock.query.filter_by(symbol=symbol).first()
    if stock_query:
        open_price = stock_query.open_price
        price_highlimit = open_price * (1 + stock_query.change_limit / 100)
        price_lowlimit = open_price * (1 - stock_query.change_limit / 100)

        ch_od_type = order_type in ['buy', 'sell']
        ch_od_amount = (0 <= amount <= 1000)
        ch_od_price = (price_lowlimit <= price <= price_highlimit)

        if ch_od_price and ch_od_amount and ch_od_type:
            order = Order(order_id, symbol, order_type, price, amount,
                          submit_time)
            current_app.logger.warning(order)
            db.session.add(order)
            db.session.commit()
            send_orders_via_queue(redis, order_id, symbol, order_type, price,
                                  amount, submit_time)
            return jsonify({'result': 'true', 'order_id': order_id})
        else:
            return jsonify({'true': 'false', 'order_id': order_id})
    else:
        return jsonify({'true': 'false', 'order_id': order_id})


@apis.route("/cancel_order.do", methods=['POST'])
@accept('application/json')
def handle_cancel_order():
    symbol = request.json.get('symbol')
    order_id = request.json.get('order_id')
    order_type = 'cancel'
    submit_time = datetime.now()

    od_query = Order.query.filter_by(symbol=symbol, order_id=order_id).first()
    current_app.logger.warning(dir(od_query))

    if od_query is None:
        return jsonify({'true': 'false', 'order_id': order_id})
    cancel_order = CancelOrder(symbol, order_id, order_type, submit_time)
    db.session.add(cancel_order)
    db.session.commit()
    return jsonify({'result': 'true', 'order_id': order_id})


def gen_order_id():
    return randrange(100000, 999999)
