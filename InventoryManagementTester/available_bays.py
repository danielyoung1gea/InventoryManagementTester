from collections import deque

class bay_stack:
    def __init__(self):
        self._elements = deque()
    def __len__(self):
        return len(self._elements)
    
    def add(self, element):
        self._elements.append(element)
    def next_bay(self):
        try:
            return self._elements.pop()
        except:
            return "No more available"
    def not_empty(self):
        if len(self._elements) > 0:
            return True
        else:
            return False

