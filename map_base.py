


from collections import MutableMapping

class MapBase(MutableMapping):
    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value
            
        def __eq__(self, other):
            return self.get_key() == other.get_key()
        
        def __ne__(self, other):
            return not (self == other)
        
        def __lt__(self, other):
            return self.get_key() < other.get_key()
        
        def get_key(self):
            return self._key
        
        def get_value(self):
            return self._value
        
        def set_value(self, newval):
            self._value = newval