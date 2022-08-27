nome = 'Henry'
print(f'{nome:*<25}')
print(f'{nome:*>25}')
print(f'{nome:>25}')
print(f'{nome:^25}')
print(f'{nome:*^25}')
print(f'{nome:_>25}')

from datetime import datetime as dt
dt.now()
data = dt.now()

print(data.strftime('%d.%m.%Y %H:%M:%S'))

print(f'{data.month}/{data.year + 4}')
print(f'{data.month:0>2}/{data.year + 4}')

from random import randint

print(randint(100,999))