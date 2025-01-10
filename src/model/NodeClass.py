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
        """
        Получение напряжения полярной системы координат
        :return: модуль напряжения
        """
        return abs(self.voltage)

    def get_polar_angle(self):
        """
        Получение угла полярной системы координат
        :return: угол в радианах
        """
        return atan(self.voltage.imag / self.voltage.real)

    def polar_to_cartesian(self, voltage, angle):
        """
        Преобразование и сохранение напряжения из полярных в декартовые координаты
        :param voltage: модуль напряжения
        :param angle: угол в радианах
        :return:
        """
        self.voltage = complex(voltage * cos(angle), voltage * sin(angle))


if __name__ == '__main__':
    pass
