from abc import ABC
import numpy
import src.utils.GlobalVariables as GV


class LinearAlgebraicEquationSolver(ABC):
    @staticmethod
    def l_a_e_s_cartesian(imbalances_s, jacobi_matrix) -> list:
        """
        Решение СЛАУ
        :param imbalances_s: список небалансов полной мощности узлов
        :param jacobi_matrix: матрица Якоби
        :return: корректировки напряжений узлов
        """
        delta = []
        for i, imb_s in enumerate(imbalances_s):
            if GV.nodes[i].type_node != 'ИП':
                delta.append(-imb_s.real)
                delta.append(-imb_s.imag)
        delta_voltage = numpy.linalg.solve(jacobi_matrix, delta)
        return [complex(delta_voltage[i], delta_voltage[i + 1]) for i in range(0, len(delta_voltage), 2)]