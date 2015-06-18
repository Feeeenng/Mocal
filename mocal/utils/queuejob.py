# -*- coding: utf-8 -*-

import os
import redis
from rq import Queue, use_connection
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
use_connection(conn)
q = Queue()


# q.enqueue(func_name, params)
