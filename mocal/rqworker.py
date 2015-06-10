# -*- coding: utf-8 -*-

import os
import redis
from rq import Queue, Worker, Connection

listen = ['high', 'default', 'low']
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

# 启动 去执行 加入队列的任务  需要redis支持