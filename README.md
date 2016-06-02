===============================
stock-trade-server
===============================

股票交易后端

**主要功能**：

- [x] 下单
    - [x] 买单
    - [x] 卖单
- [x] 撤单
- [x] 股票限价，限量交易

**下单接口**

- 交易订单
```
curl -i -X POST \
   -H "Content-Type: application/json; indent=4" \
   -d '{
    "symbol": "WSCN",
    "order_type": "buy",
    "price": 100,
    "amount": 100
}' http://192.168.33.10:8000/trade.do
```

- 撤销订单
```
$ curl -i -X POST \
    -H "Content-Type: application/json; indent=4" \
    -d '{
    "symbol": "WSCN",
    "order_id": 1000
}' http://192.168.33.10:8000/cancel_order.do
```

**其他**：

补充说明：

- 订单接口基于Flask
- 交易内核基于celery和redis， 生产者、消费者模式
- 结果存储数据库，默认sqlite3

## 快速开始

安装 MySQL、Redis、Celery
```
略
```

创建配置文件
```
vi config.py
```

初始化数据库

```
>>> python manager.py db init
>>> python manager.py db migrate -m "init"
>>> python manager.py upgrade
```

运行

```
python manager.py runserver
```

Shell

```
python manager.py shell
```

数据库升级

```
python manage.py db migrate
python manage.py db upgrade
```

运行队列任务

```
celery worker -A celery_worker.celery --loglevel=info
```

测试

```
这个开发者很懒，暂时没写下什么测试……
```

部署

```
# using gunicorn
pip install gunicorn

# run
gunicorn -w 4 -p trader.pid -b 0.0.0.0:8000 manager:app -D --log-level warning --error-logfile gunicorn-error.log

# reload
kill -HUP `cat trader.pid`
```

## License
[MIT](LICENSE)
