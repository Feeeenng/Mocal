# -*- coding: utf-8 -*-

import os
import redis
from rq import Queue, Connection, Worker
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

listen = ['high', 'default', 'low']

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

# 启动 去执行 加入队列的任务  需要redis支持