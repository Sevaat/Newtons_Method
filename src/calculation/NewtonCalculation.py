from abc import ABC
from src.calculation.ModeCalculationDataClass import ModeCalculationData as MCD
import src.GlobalVariables as GV
import numpy


class NewtonClass(ABC):
    @staticmethod
    def calculation():
        """
        Расчет методом ньютона установившегося режима электрической сети
        :return:
        """
        y_matrix = MCD.get_y_matrix()
        for i in range(0, GV.OPTIONS.number_of_iterations):
            imbalances_s = MCD.get_imbalances_s(y_matrix)
            if MCD.unbalance_condition(imbalances_s):
                print('Точность достигнута! Расчет окончен!')
                break
            jacobi_matrix = NewtonClass.get_jacobi_matrix(y_matrix)
            delta_voltage = NewtonClass.linear_algebraic_equation_solver(imbalances_s, jacobi_matrix)
            NewtonClass.voltage_correction(delta_voltage)

    @staticmethod
    def get_jacobi_matrix(y_matrix: numpy.ndarray) -> numpy.ndarray:
        """
        Получение матрицы Якоби
        :param y_matrix: матрица собственных и взаимных проводимостей узлов
        :return: матрица Якоби
        """
        node_count = len(GV.nodes)
        jacobi_matrix = []
        for i in range(node_count):
            if GV.nodes[i].type_node != 'ИП':
                dp_u = []
                dq_u = []
                for j in range(node_count):
                    if GV.nodes[j].type_node != 'ИП':
                        pur = 0
                        pui = 0
                        qur = 0
                        qui = 0
                        if i == j:
                            for k in range(node_count):
                                if k != j:
                                    pur += y_matrix[i, k].real * GV.nodes[k].voltage.real + y_matrix[i, k].imag * \
                                           GV.nodes[k].voltage.imag
                                    pui += y_matrix[i, k].real * GV.nodes[k].voltage.imag - y_matrix[i, k].imag * \
                                           GV.nodes[k].voltage.real
                                    qur += y_matrix[i, k].real * GV.nodes[k].voltage.imag - y_matrix[i, k].imag * \
                                           GV.nodes[k].voltage.real
                                    qui += y_matrix[i, k].real * GV.nodes[k].voltage.real + y_matrix[i, k].imag * \
                                           GV.nodes[k].voltage.imag
                            pur = -2 * y_matrix[i, i].real * GV.nodes[i].voltage.real - pur
                            pui = -2 * y_matrix[i, i].real * GV.nodes[i].voltage.imag - pui
                            qur = 2 * y_matrix[i, i].imag * GV.nodes[i].voltage.real - qur
                            qui = 2 * y_matrix[i, i].imag * GV.nodes[i].voltage.imag + qui
                        else:
                            pur = -y_matrix[i, j].real * GV.nodes[j].voltage.real + y_matrix[i, j].imag * GV.nodes[
                                j].voltage.imag
                            pui = -y_matrix[i, j].imag * GV.nodes[j].voltage.real - y_matrix[i, j].real * GV.nodes[
                                j].voltage.imag
                            qur = y_matrix[i, j].imag * GV.nodes[j].voltage.real + y_matrix[i, j].real * GV.nodes[
                                j].voltage.imag
                            qui = -y_matrix[i, j].real * GV.nodes[j].voltage.real + y_matrix[i, j].imag * GV.nodes[
                                j].voltage.imag
                        dp_u.append(pur)
                        dp_u.append(pui)
                        dq_u.append(qur)
                        dq_u.append(qui)
                jacobi_matrix.append(dp_u)
                jacobi_matrix.append(dq_u)
        return numpy.array(jacobi_matrix)

    @staticmethod
    def linear_algebraic_equation_solver(imbalances_s, jacobi_matrix) -> list:
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

    @staticmethod
    def voltage_correction(delta_voltage):
        """
        Корректировка напряжений узлов
        :param delta_voltage: корректировки напряжений узлов
        :return: скорректированные напряжения узлов
        """
        j = 0
        for i in range(len(GV.nodes)):
            if GV.nodes[i].type_node != 'ИП':
                GV.nodes[i].voltage = GV.nodes[i].voltage + delta_voltage[j]
                j += 1


if __name__ == '__main__':
    pass
