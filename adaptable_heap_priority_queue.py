'''
Problem: Implement a heap-based priority queue, with ability to remove elements from arbitrary locations (not just min element)
'''



from heap_priority_queue_array import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    
    class _Locator(HeapPriorityQueue._Item):
        def __init__(self, key, value, index):
            super.__init__(key, value)
            self._index = index
            
        def get_index(self):
            return self._index
        
        def set_index(self, index):
            self._index = index
            
    def _swap(self, i, j):
        super._swap(i, j)
        self._data[i].set_index(i)
        self._data[j].set_index(j)
        
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent[j]]:
            self._upheap(j)
        else:
            self._downheap(j)
            
    def add(self, key, value):
        token = self._Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token
    
    def update(self, loc, newkey, newval):
        j = loc.get_index()
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator!')
        loc.set_key(newkey)
        loc.set_value(newval)
        self._bubble(j)
        
    def remove(self, loc):
        j = loc.get_index()
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator!')
        if j == len(self._data) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc.get_key(), loc.get_value())