# -*- coding: utf-8 -*-

from datetime import datetime
from . import db


class Order(db.Model):
    __table_name__ = 'trade_orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    order_type = db.Column(db.String(4), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    submit_time = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def __init__(self, order_id, symbol, order_type, price, amount,
                 submit_time):
        self.order_id = order_id
        self.symbol = symbol
        self.order_type = order_type
        self.price = price
        self.amount = amount
        self.submit_time = submit_time

    def __repr__(self):
        return '<orderid %r>' % self.order_id

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()
        return self

    def as_dictionary(self):
        post = {
            "id": self.id,
            "title": self.title,
            "body": self.body
        }
        return post


class Stock(db.Model):
    __table_name__ = 'trading_stocks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    symbol = db.Column(db.String(10), nullable=False)
    open_price = db.Column(db.Integer, nullable=False)
    close_price = db.Column(db.Integer, nullable=False)
    change_limit = db.Column(db.Integer, nullable=False)


class CancelOrder(db.Model):
    __table_name__ = 'canceled_orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    order_type = db.Column(db.String(10), nullable=True)
