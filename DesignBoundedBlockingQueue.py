import threading

class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self.capacity = capacity
        
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.editing = threading.Lock()
      
        self.queue = collections.deque()

    def enqueue(self, element):
        self.pushing.acquire()
        self.editing.acquire()

        self.queue.append(element)

        self.editing.release()
        self.pulling.release()

    def dequeue(self):
        self.pulling.acquire()
        self.editing.acquire()
        
        res = self.queue.popleft()
        
        self.editing.release()
        self.pushing.release()
        return res

    def size(self):
        return len(self.queue)
    
#     The idea is to use two semaphores, pushing and pulling, to maintain the invariants of the queue.
# Initially, no thread can dequeue (self.pulling.acquire()) until a thread has enqueued (self.pulling.release()).
# When capacity elements have been enqueued, self.pushing.acquire() will block the thread until a dequeue releases the semaphore again.
# Additionally, use a Lock so only a single thread can modify the actual queue at once.
