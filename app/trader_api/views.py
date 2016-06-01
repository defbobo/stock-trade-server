# -*- coding: utf-8 -*-

from flask import request, jsonify, abort
from datetime import datetime
from . import apis
from .. import db
from ..models import Order, Stock, CancelOrder
from ..decorators import accept

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

    if Stock.query.filter_by(symbol=symbol).first() is None:
        return jsonify({'result': 'false', 'order_id': order_id})
    if order_type not in ['buy', 'sell']:
        return jsonify({'result': 'false', 'order_id': order_id})
    if amount < 0 or amount > 1000:
        return jsonify({'result': 'false', 'order_id': order_id})

    submit_time = datetime.now()
    order = Order(order_id, symbol, order_type, price, amount, submit_time)
    db.session.add(order)
    return jsonify({'result': 'true', 'order_id': order_id})


@apis.route("/cancel_order.do", methods=['POST'])
@accept('application/json')
def handle_cancel_order():
    symbol = request.json.get('symbol')
    order_id = request.json.get('order_id')
    order_type = 'cancel'

    if Order.query.filter_by(symbol=symbol, order_id=order_id).first() is None:
        abort(400)
    cancel_order = CancelOrder(symbol, order_id, order_type)
    db.session.add(cancel_order)
    return jsonify({'result': 'true', 'order_id': order_id})

def gen_order_id():
    return 1000
