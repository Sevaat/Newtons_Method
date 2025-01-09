from math import *


class Node:
    def __init__(self):
        self.s_power = None  # комплексная полная мощность узла (заданная)
        self.voltage = None  # фактическое комплексное напряжение узла
        self.type_node = None  # тип узла: источник питания, источник ограниченной мощности, нагрузка
        self.name = None  # имя узла

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

    def get_polar_voltage(self):
        '''
        Перевод напряжения в полярную систему координат
        :return: модуль напряжения, угол в радианах
        '''
        voltage = abs(self.voltage)
        angle = atan(self.voltage.imag / self.voltage.real)
        return voltage, angle

    def polar_to_cartesian(self, voltage, angle):
        '''
        Преобразование и сохранение напряжения из полярных в декартовые координаты
        :return:
        '''
        real = voltage * cos(angle)
        imag = voltage * sin(angle)
        self.voltage = complex(real, imag)


if __name__ == '__main__':
    pass
