


class PriorityQueueBase:
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._val = value
            
        def __lt__(self, other):
            return self._key < other._key
        
        def get_key(self):
            return self._key
        
        def set_key(self, key):
            self._key = key
            
        def get_value(self):
            return self._val
        
        def set_value(self, value):
            self._val = value
            
    def is_empty(self):
        return len(self) == 0