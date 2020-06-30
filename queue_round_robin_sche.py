'''
Problem: Implement a round-robin scheduler with a specific timeout
'''


# Caution: The following implementation is by no means complete, it is just a simple example

from sll_queue import SllQueue
from sll_queue import QueueEmpty
import threading
import time


# General structure of scheduled jobs
class Job:
    def __init__(self, description = ''):
        self._description = description
        # Caution: there are different ways to kill a thread in Python. Here, I use the simplest way. Based on your application,
        # you might prefer a different method. 
        self._stop = False 
        
    def __str__(self):
        return self._description
    
    def job(self):
        while not self._stop:
            print(self)
            time.sleep(1)
    
    def start(self):
        thread = threading.Thread(target = self.job)
        self._stop = False
        thread.start()
        
    def stop(self):
        self._stop = True
    
    
class RRScheduler:
    # Timeout in seconds
    def __init__(self, timeout = 3.0):
        self._timeout = timeout
        self._q = SllQueue()
        self._timer = None
        self._current = None
        self._cancel = False
        self._mutex = threading.Lock()
        
    def __len__(self, ):
        return len(self._q)
        
    def _sched(self):
        if self._q.is_empty():
            raise QueueEmpty('There is no jobs to run, add some jobs first!')
        # Event loop
        while True:
            # For stopping the scheduler
            if self._cancel:
                break
            self._current = self.remove_job()
            self._current.start()
            time.sleep(self._timeout)
            self._current.stop()
            self.add_job(self._current)
        
    def add_job(self, job):
        self._mutex.acquire()
        self._q.enqueue(job)
        self._mutex.release()
        
    def remove_job(self):
        self._mutex.acquire()
        job = self._q.dequeue()
        self._mutex.release()
        return job
    
    def start(self):
        self._cancel = False
        self._timer = threading.Thread(target = self._sched)
        self._timer.start()
        self._timer.join()
    
    def cancel(self):
        self._cancel = True


# A simple test
def test_run(wait = 10, jobs = 3, runs = 1):
    sched = RRScheduler()
    for i in range(jobs):
        j = Job("job" + str(i + 1))
        sched.add_job(j)
    
    for i in range(runs):
        print("Starting run number %d:" % (i + 1))    
        sched_thread = threading.Thread(target = sched.start)
        sched_thread.start()
        time.sleep(wait)
        sched.cancel()
        sched_thread.join()

test_run(runs = 2)