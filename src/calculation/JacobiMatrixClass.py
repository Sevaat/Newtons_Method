from abc import ABC
import numpy
import src.utils.GlobalVariables as GV
from math import *


class JacobiMatrix(ABC):
    @staticmethod
    def get_jacobi_matrix_cartesian(y_matrix: numpy.ndarray) -> numpy.ndarray:
        """
        Получение матрицы Якоби в декартовых координатах
        :param y_matrix: матрица собственных и взаимных проводимостей узлов
        :return: матрица Якоби
        """
        jacobi_matrix = []
        for i in range(len(GV.nodes)): # номер мощности
            if GV.nodes[i].type_node != 'ИП':
                row_pi_jacobi_matrix = JacobiMatrix.get_row_pi_jacobi_matrix_cartesian(i, y_matrix)
                jacobi_matrix.append(row_pi_jacobi_matrix)
                row_qi_jacobi_matrix = JacobiMatrix.get_row_qi_jacobi_matrix_cartesian(i, y_matrix)
                jacobi_matrix.append(row_qi_jacobi_matrix)
        return numpy.array(jacobi_matrix)

    @staticmethod
    def get_row_pi_jacobi_matrix_cartesian(i: int, y_matrix: numpy.ndarray):
        row_pi_jm = []
        for j in range(len(GV.nodes)): # номер напряжения
            if GV.nodes[j].type_node != 'ИП':
                dpi_du = JacobiMatrix.get_dpi_du_cartesian(i, j, y_matrix)
                row_pi_jm.append(dpi_du[0])
                row_pi_jm.append(dpi_du[1])
        return row_pi_jm

    @staticmethod
    def get_dpi_du_cartesian(i: int, j: int, y_matrix: numpy.ndarray):
        if i == j:
            dpi_dui_real = [0, 0]
            dpi_dui_imag = [0, 0]
            dpi_dui_real[0] = 2 * y_matrix[i, i].real * GV.nodes[i].voltage.real
            dpi_dui_imag[0] = 2 * y_matrix[i, i].real * GV.nodes[i].voltage.imag
            for k in range(len(GV.nodes)): # номер позиции под знаком суммы
                if k != i:
                    dpi_dui_real[1] += y_matrix[i, k].real * GV.nodes[k].voltage.real
                    dpi_dui_real[1] -= y_matrix[i, k].imag * GV.nodes[k].voltage.imag
                    dpi_dui_imag[1] += y_matrix[i, k].real * GV.nodes[k].voltage.imag
                    dpi_dui_imag[1] += y_matrix[i, k].imag * GV.nodes[k].voltage.real
            dpi_dui_real = dpi_dui_real[0] + dpi_dui_real[1]
            dpi_dui_imag = dpi_dui_imag[0] + dpi_dui_imag[1]
            return dpi_dui_real, dpi_dui_imag
        else:
            dpi_duj_real = y_matrix[i, j].real * GV.nodes[i].voltage.real
            dpi_duj_real += y_matrix[i, j].imag * GV.nodes[i].voltage.imag
            dpi_duj_imag = y_matrix[i, j].real * GV.nodes[i].voltage.imag
            dpi_duj_imag -= y_matrix[i, j].imag * GV.nodes[i].voltage.real
            return dpi_duj_real, dpi_duj_imag

    @staticmethod
    def get_row_qi_jacobi_matrix_cartesian(i: int, y_matrix: numpy.ndarray):
        row_qi_jm = []
        for j in range(len(GV.nodes)):  # номер напряжения
            if GV.nodes[j].type_node != 'ИП':
                dqi_du = JacobiMatrix.get_dqi_du_cartesian(i, j, y_matrix)
                row_qi_jm.append(dqi_du[0])
                row_qi_jm.append(dqi_du[1])
        return row_qi_jm

    @staticmethod
    def get_dqi_du_cartesian(i: int, j: int, y_matrix: numpy.ndarray):
        if i == j:
            dqi_dui_real = [0, 0]
            dqi_dui_imag = [0, 0]
            dqi_dui_real[0] = - 2 * y_matrix[i, i].imag * GV.nodes[i].voltage.real
            dqi_dui_imag[0] = - 2 * y_matrix[i, i].imag * GV.nodes[i].voltage.imag
            for k in range(len(GV.nodes)):  # номер позиции под знаком суммы
                if k != i:
                    dqi_dui_real[1] += y_matrix[i, k].real * GV.nodes[k].voltage.imag
                    dqi_dui_real[1] += y_matrix[i, k].imag * GV.nodes[k].voltage.real
                    dqi_dui_imag[1] += y_matrix[i, k].real * GV.nodes[k].voltage.real
                    dqi_dui_imag[1] -= y_matrix[i, k].imag * GV.nodes[k].voltage.imag
            dqi_dui_real = dqi_dui_real[0] - dqi_dui_real[1]
            dqi_dui_imag = dqi_dui_imag[0] + dqi_dui_imag[1]
            return dqi_dui_real, dqi_dui_imag
        else:
            dqi_duj_real = y_matrix[i, j].real * GV.nodes[i].voltage.imag
            dqi_duj_real -= y_matrix[i, j].imag * GV.nodes[i].voltage.real
            dqi_duj_imag = - y_matrix[i, j].real * GV.nodes[i].voltage.real
            dqi_duj_imag -= y_matrix[i, j].imag * GV.nodes[i].voltage.imag
        return dqi_duj_real, dqi_duj_imag

    @staticmethod
    def get_jacobi_matrix_polar(y_matrix: numpy.ndarray) -> numpy.ndarray:
        """
        Получение матрицы Якоби в полярных координатах
        :param y_matrix: матрица собственных и взаимных проводимостей узлов
        :return: матрица Якоби
        """
        jacobi_matrix = []
        for i in range(len(GV.nodes)):  # номер мощности
            if GV.nodes[i].type_node != 'ИП':
                row_pi_jacobi_matrix = JacobiMatrix.get_row_pi_jacobi_matrix_polar(i, y_matrix)
                jacobi_matrix.append(row_pi_jacobi_matrix)
                row_qi_jacobi_matrix = JacobiMatrix.get_row_qi_jacobi_matrix_polar(i, y_matrix)
                jacobi_matrix.append(row_qi_jacobi_matrix)
        return numpy.array(jacobi_matrix)

    @staticmethod
    def get_row_pi_jacobi_matrix_polar(i: int, y_matrix: numpy.ndarray):
        row_pi_jm = []
        for j in range(len(GV.nodes)):  # номер напряжения
            if GV.nodes[j].type_node != 'ИП':
                dpi_du = JacobiMatrix.get_dpi_du_polar(i, j, y_matrix)
                row_pi_jm.append(dpi_du[0])
                row_pi_jm.append(dpi_du[1])
        return row_pi_jm

    @staticmethod
    def get_dpi_du_polar(i: int, j: int, y_matrix: numpy.ndarray):
        u_i = GV.nodes[i].get_polar_voltage()
        b_i = GV.nodes[i].get_polar_angle()
        u_j = GV.nodes[j].get_polar_voltage()
        b_j = GV.nodes[j].get_polar_angle()
        if i == j:
            dpi_dui = [0, 0]
            dpi_dbi = 0
            dpi_dui[0] = 2 * y_matrix[i, i].real * u_i
            for k in range(len(GV.nodes)):  # номер позиции под знаком суммы
                if k != i:
                    u_k = GV.nodes[k].get_polar_voltage()
                    b_k = GV.nodes[k].get_polar_angle()
                    dpi_dui[1] += u_k * (y_matrix[i, k].real * cos(b_i - b_k) + y_matrix[i, k].imag * sin(b_i - b_k))
                    dpi_dbi += u_k * (y_matrix[i, k].real * sin(b_k - b_i) + y_matrix[i, k].imag * cos(b_i - b_k))
            dpi_dui = dpi_dui[0] + dpi_dui[1]
            dpi_dbi = u_i * dpi_dbi
            return dpi_dui, dpi_dbi
        else:
            dpi_duj = u_i * (y_matrix[i, j].real * cos(b_i - b_j) + y_matrix[i, j].imag * sin(b_i - b_j))
            dpi_dbj = u_i * u_j * (y_matrix[i, j].real * sin(b_i - b_j) - y_matrix[i, j].imag * cos(b_i - b_j))
            return dpi_duj, dpi_dbj

    @staticmethod
    def get_row_qi_jacobi_matrix_polar(i: int, y_matrix: numpy.ndarray):
        row_qi_jm = []
        for j in range(len(GV.nodes)):  # номер напряжения
            if GV.nodes[j].type_node != 'ИП':
                dqi_du = JacobiMatrix.get_dqi_du_polar(i, j, y_matrix)
                row_qi_jm.append(dqi_du[0])
                row_qi_jm.append(dqi_du[1])
        return row_qi_jm

    @staticmethod
    def get_dqi_du_polar(i: int, j: int, y_matrix: numpy.ndarray):
        u_i = GV.nodes[i].get_polar_voltage()
        b_i = GV.nodes[i].get_polar_angle()
        u_j = GV.nodes[j].get_polar_voltage()
        b_j = GV.nodes[j].get_polar_angle()
        if i == j:
            dqi_dui = [0, 0]
            dqi_dbi = 0
            dqi_dui[0] = - 2 * y_matrix[i, i].imag * u_i
            for k in range(len(GV.nodes)):  # номер позиции под знаком суммы
                if k != i:
                    u_k = GV.nodes[k].get_polar_voltage()
                    b_k = GV.nodes[k].get_polar_angle()
                    dqi_dui[1] += u_k * (y_matrix[i, k].real * sin(b_i - b_j) - y_matrix[i, k].imag * cos(b_i - b_k))
                    dqi_dbi += u_k * (y_matrix[i, k].real * cos(b_i - b_k) - y_matrix[i, k].imag * sin(b_k - b_i))
            dqi_dui = dqi_dui[0] + dqi_dui[1]
            dqi_dbi = u_i * dqi_dbi
            return dqi_dui, dqi_dbi
        else:
            dqi_duj = u_i * (y_matrix[i, j].real * sin(b_i - b_j) - y_matrix[i, j].imag * cos(b_i - b_j))
            dqi_dbj = u_i * u_j * (- y_matrix[i, j].real * cos(b_i - b_j) - y_matrix[i, j].imag * sin(b_i - b_j))
            return dqi_duj, dqi_dbj