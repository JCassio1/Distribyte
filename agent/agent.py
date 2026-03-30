import threading
from time import sleep

class Agent:
    def __init__(self, name, max_capacity):
        self._name = name
        self._max_capacity = max_capacity
        self._tasks = []
        self._lock = threading.Lock()
        self._running = False

    def run(self, poll_interval: float = 1.0):
        self._running = True
        print(f"{self._name} is running with capacity {self.current_capacity}.")
        while self._running:
            sleep(poll_interval)

    def stop(self, name):
        if (name == self._name):
            self._running = False
            print(f"{self._name} has stopped.")
    

    @property
    def name(self):
        return self._name
    
    @property
    def max_capacity(self):
        return self._max_capacity
    
    @property
    def current_capacity(self):
        return f"{len(self._tasks)}/{self._max_capacity}"
    
    @property
    def is_available(self):
        if len(self._tasks) >= self._max_capacity:
            return False

        return True
    
    @property
    def tasks(self):
        return self._tasks
    
    def add_task(self, task):
        if self.is_available and task not in self._tasks and task is not None:
            with self._lock:
                self._tasks.append(task)
                print(f"Task '{task}' added to {self._name}. Current load: {self.current_capacity}")
                return True
        return False
    
    def remove_task(self, task):
        if task in self._tasks:
            with self._lock:
                print(f"Task '{task}' removed from {self._name}. Current load: {self.current_capacity}")
                self._tasks.remove(task)
                return True
        return False

