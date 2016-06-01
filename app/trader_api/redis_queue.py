# -*- coding: utf-8 -*-
import json

def send_orders_via_queue(conn, order_id, symbol, order_type, price, amount,
                          submit_time):
    data = {
        'order_id': order_id,
        'symbol': symbol,
        'order_type': order_type,
        'price': price,
        'amount': amount,
        'submit_time': submit_time
    }
    conn.rpush('queue:trade', json.dumps(data))
