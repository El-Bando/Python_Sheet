myset = {4, 12, 77, 120}
myset.add('elem')
myset.remove(120)
myset.pop()
myset.discard('nothing')
print(f'myset = {myset}')
aset = myset.copy()
myset.clear()
print(f'myset = {myset}')
print(f'aset = {aset}')