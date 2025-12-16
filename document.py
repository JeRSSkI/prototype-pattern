import copy

class Document:
    def clone(self):
        return copy.copy(self)
