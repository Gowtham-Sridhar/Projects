from pathlib import Path

path = Path()
# print(path.glob('*.xlsx'))
# <generator object Path.glob at 0x7f39800da5c8>

for file in path.glob('*.py'):
    print(file)
