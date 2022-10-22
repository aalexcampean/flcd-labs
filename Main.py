from SymbolTable import SymbolTable


if __name__ == "__main__":
    symbolTable = SymbolTable()
    symbolTable.add('lol', 4)
    symbolTable.add('sdfgdh', 5)
    symbolTable.add('idk', 1)
    assert('idk' in symbolTable)
    symbolTable.delete('idk')
    symbolTable.add('scdc', 3)