# Пример 1.16.PP4E\Preview\manager.py

"""
Пример 1.16
специализирует предыдущий класс Person, предусматривая 10-процентную надбавку, добавляемую при увеличении оклада менеджеров
(любые совпадения с реальными примерами из жизни являются случайными).
"""
from person import Person

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)