



from map_base import MapBase
from random import randrange

class HashMapBase(MapBase):
    def __init__(self, cap = 11, p = 109345121):
        self._table = [None] * cap
        self._n = 0                             # Number of stored entries in map
        self._prime = p                         # Prime number for MAD compression
        self._scale = 1 + randrange(p - 1)      # Scale from 1 to p-1 for MAD
        self._shift = randrange(p)              # Shift from 1 to p -1 for MAD
        
    def _hash_function(self, key):
        return (hash(key) * self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, key):
        j = self._hash_function(key)
        return self._bucket_getitem(j, key)
    
    def __setitem__(self, key, value):
        j = self._hash_function(key)
        self._bucket_setitem(j, key, value)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
            
    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)
        self._n -= 1
        
    def _resize(self, n):
        old = list(self.items())
        self._table = n * [None]
        self._n = 0     # N will be recomputed using subsequent adds
        for (k, v) in old:
            self[k] = v
        