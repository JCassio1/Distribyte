class agent:
    def __init__(self, name, max_capacity):
        self._name = name
        self._max_capacity = max_capacity
        self._tasks = []

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
            self._tasks.append(task)
            return True
        return False
    
    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            return True
        return False

