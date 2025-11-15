from faker import Faker

gerador = Faker

for i in range(10):
    print(gerador.name())
    print(gerador.adress())
    print('#' * 5)




'''



@greg0059
há 7 horas
```python
from faker import Faker

fake = Faker('pt_BR')
for _ in range(10):
    print(fake.name())
```
Gera nomes brasileiros falsos

'''