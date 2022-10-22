from HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.hasTable = HashTable()

    def add(self, key, value):
        self.hasTable.insert(key, value)

    def delete(self, key):
        return self.hasTable.remove(key)

    def find(self, key):
        return self.hasTable.find(key)

    def __contains__(self, key):
        return key in self.hasTable
