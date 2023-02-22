import faker
# генерация в цикле произвольных значений ( применение как наполнение БД)
from faker import Faker
fake =Faker(locale='ru_Ru')
for _ in range(10) :
    print(fake.name())
    print(fake.address())
    print(fake.text())
    print(fake.job())
