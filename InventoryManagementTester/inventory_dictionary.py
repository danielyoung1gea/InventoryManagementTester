from collections import deque

class inventory_dictionary:
    def __init__(self):
        all_types = ["FD FZ GY","FD FZ WW", "FD FF GY", "FD FF WW", "CD FZ GY","CD FZ WW", "CD FF GY", "CD FF WW"]
        self._elements = {}
        for t in all_types:
            self._elements.update({t:deque()})
    def __len__(self):
        return len(self._elements)
    def add_to_inventory(self, sheet_type, pallet):
        self._elements[sheet_type].append(pallet)
    def get_next(self, sheet_type):
        if len(self._elements[sheet_type]) > 0:
            return self._elements[sheet_type].popleft()
        else: return 0
