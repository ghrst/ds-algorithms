


from map_base import MapBase

class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []
        
    def __setitem__(self, key, value):
        for item in self._table:
            if item.get_key() == key:
                item.set_value(value)
                return
        self._table.append(self._Item(key, value))
        
    def __getitem__(self, key):
        for item in self._table:
            if item.get_key() == key:
                return item.get_value()
        raise KeyError('Your requested key: %s does not exists' % (str(key)))
    
    def __delitem__(self, key):
        for j in range(len(self._table)):
            if self._table[j].get_key() == key:
                self._table.pop(j)
                return
        raise KeyError('Your requested key: %s does not exists' % (str(key)))
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item.get_key()