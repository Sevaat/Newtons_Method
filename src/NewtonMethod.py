from abc import ABC
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix


def newton_method():
    """
    Расчет методом ньютона установившегося режима электрической сети
    :return:
    """
    y_matrix = YMatrix.get_y_matrix()
    for i in range(0, GV.OPTIONS.number_of_iterations):
        imbalances_s = GV.NEWTONMETHOD.imbalance_calculation(y_matrix)
        if GV.NEWTONMETHOD.unbalance_condition(imbalances_s):
            print('Точность достигнута! Расчет окончен!')
            break
        jacobi_matrix = GV.NEWTONMETHOD.jacoby_matrix_calculation(y_matrix)
        delta_voltage = GV.NEWTONMETHOD.linear_algebraic_equation_solver(imbalances_s, jacobi_matrix)
        GV.NEWTONMETHOD.voltage_correction(delta_voltage)


if __name__ == '__main__':
    pass
