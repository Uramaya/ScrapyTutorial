from queue import Queue
# 使用
q = Queue()
q.put(url)
q.get() # 当队列为空时，阻塞
q.get(block=True,timeout=3) # 超过3秒抛异常
q.get(block=False) # 为空时直接抛异常
q.empty()