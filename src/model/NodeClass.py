class Node:
    def __init__(self):
        self.s_power = None # комплексная полная мощность узла (заданная)
        self.voltage = None # фактическое комплексное напряжение узла
        self.type_node = None # тип узла: источник питания, источник ограниченной мощности, нагрузка
        self.name = None # имя узла

    def __str__(self):
        return f'''Имя узла: {self.name}
Тип узла: {self.type_node}
Комплексная полная мощность узла (заданная): {self.s_power} МВА
Фактическое комплексное напряжение узла: {self.voltage} кВ
Модуль фактического комплексного напряжения узла: {abs(self.voltage)} кВ

'''

    def __repr__(self):
        return f'''Имя узла: {self.name}
Тип узла: {self.type_node}
Комплексная полная мощность узла (заданная): {self.s_power} МВА
Фактическое комплексное напряжение узла: {self.voltage} кВ
Модуль фактического комплексного напряжения узла: {abs(self.voltage)} кВ

'''


if __name__ == '__main__':
    pass
