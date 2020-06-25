'''
Problem: Implement a stack using Python list as the underlying structure. For more information about stack ADT refer to:
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
'''


class StackEmpty(Exception):
    """ When someone attempts to pop or top the stack when it is empty this exception will be risen """
    pass


class ListStack:
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, item):
        self._data.append(item)
        
    def pop(self):
        if self.is_empty():
            raise StackEmpty('Stack is empty!')
        return self._data.pop()
    
    def top(self):
        if self.is_empty():
            raise StackEmpty('Stack is empty!')
        return self._data[-1]
    
