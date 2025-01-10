from abc import ABC
import numpy
import src.utils.GlobalVariables as GV
from math import *


class Imbalances(ABC):
    @staticmethod
    def get_imbalances_s_cartesian(y_matrix: numpy.ndarray) -> list:
        """
        Получение небалансов полной мощности узлов в декартовых координатах
        :param y_matrix: матрица собственных и взаимных проводимостей узлов
        :return: список небалансов полной мощности узлов
        """
        node_count = len(GV.nodes)
        imbalances_s = []
        for i in range(node_count):
            s_power = None
            if GV.nodes[i].type_node == 'ИП':
                s_power = complex(0, 0)
            elif GV.nodes[i].type_node == 'ИОМ':
                s_power = -GV.nodes[i].s_power
            else:
                s_power = GV.nodes[i].s_power
            p = [0, 0, 0]
            p[0] = s_power.real + y_matrix[i, i].real * GV.nodes[i].get_polar_voltage() ** 2
            q = [0, 0, 0]
            q[0] = s_power.imag - y_matrix[i, i].imag * GV.nodes[i].get_polar_voltage() ** 2
            for j in range(node_count):
                if j != i:
                    p[1] += y_matrix[i, j].real * GV.nodes[j].voltage.real
                    p[1] -= y_matrix[i, j].imag * GV.nodes[j].voltage.imag
                    p[2] += y_matrix[i, j].real * GV.nodes[j].voltage.imag
                    p[2] += y_matrix[i, j].imag * GV.nodes[j].voltage.real
                    q[1] += y_matrix[i, j].real * GV.nodes[j].voltage.real
                    q[1] -= y_matrix[i, j].imag * GV.nodes[j].voltage.imag
                    q[2] += y_matrix[i, j].real * GV.nodes[j].voltage.imag
                    q[2] += y_matrix[i, j].imag * GV.nodes[j].voltage.real
            p[1] = GV.nodes[i].voltage.real * p[1]
            p[2] = GV.nodes[i].voltage.imag * p[2]
            q[1] = GV.nodes[i].voltage.imag * q[1]
            q[2] = - GV.nodes[i].voltage.real * q[2]
            imbalances_s.append(complex(sum(p), sum(q)))
        return imbalances_s

    @staticmethod
    def get_imbalances_s_polar(y_matrix: numpy.ndarray) -> list:
        """
        Получение небалансов полной мощности узлов в полярных координатах
        :param y_matrix: матрица собственных и взаимных проводимостей узлов
        :return: список небалансов полной мощности узлов
        """
        node_count = len(GV.nodes)
        imbalances_s = []
        for i in range(node_count):
            s_power = None
            if GV.nodes[i].type_node == 'ИП':
                s_power = complex(0, 0)
            elif GV.nodes[i].type_node == 'ИОМ':
                s_power = -GV.nodes[i].s_power
            else:
                s_power = GV.nodes[i].s_power
            u_i = GV.nodes[i].get_polar_voltage()
            b_i = GV.nodes[i].get_polar_angle()
            p = [0, 0]
            p[0] = s_power.real + y_matrix[i, i].real * u_i ** 2
            q = [0, 0]
            q[0] = s_power.imag - y_matrix[i, i].imag * u_i ** 2
            for j in range(node_count):
                if j != i:
                    u_j = GV.nodes[j].get_polar_voltage()
                    b_j = GV.nodes[j].get_polar_angle()
                    p[1] += u_j * (y_matrix[i, j].real * cos(b_i - b_j) + y_matrix[i, j].imag * sin(b_i - b_j))
                    q[1] += u_j * (y_matrix[i, j].real * sin(b_i - b_j) - y_matrix[i, j].imag * cos(b_i - b_j))
            p[1] = u_i * p[1]
            q[1] = u_i * q[1]
            imbalances_s.append(complex(sum(p), sum(q)))
        return imbalances_s
