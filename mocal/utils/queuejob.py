# -*- coding: utf-8 -*-

from rq import Queue, use_connection
from rqworker import conn

use_connection(conn)
q = Queue()


# q.enqueue(func_name, params)
