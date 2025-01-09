class Options:
    def __init__(self):
        self.nominal_voltage = None # номинальное напряжение сети
        self.precision = None # точность расчета
        self.number_of_iterations = None # количество итераций МН

    def __str__(self):
        return f'''Номинальное напряжение сети: {self.nominal_voltage} кВ
Точность расчета: {self.precision} МВА
Количество итераций МН: {self.number_of_iterations}

'''

    def __repr__(self):
        return f'''Номинальное напряжение сети: {self.nominal_voltage} кВ
Точность расчета: {self.precision} МВА
Количество итераций МН: {self.number_of_iterations}

'''


if __name__ == '__main__':
    pass
