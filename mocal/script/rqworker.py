# -*- coding: utf-8 -*-

from rq import Queue, Worker, Connection
from utils.queuejob import conn

listen = ['high', 'default', 'low']

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

# 启动 去执行 加入队列的任务  需要redis支持