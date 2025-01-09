from abc import ABC
import numpy
import src.GlobalVariables as GV


class ModeCalculationData(ABC):
    @staticmethod
    def get_y_matrix() -> numpy.ndarray:
        """
        Получение матрицы собственных и взаимных проводимостей узлов
        :return: матрица собственных и взаимных проводимостей узлов
        """
        y_matrix = numpy.array([1 / branch.z_resistance for branch in GV.branches])
        incident_matrix = ModeCalculationData.get_incident_matrix()
        y_matrix = numpy.dot(incident_matrix, numpy.diag(y_matrix))
        y_matrix = numpy.dot(y_matrix, incident_matrix.transpose())
        b_conductivity = []
        for i in range(len(GV.nodes)):
            b = 0
            for j in range(len(GV.branches)):
                if incident_matrix[i, j] != 0.:
                    b += GV.branches[j].b_conductivity
            b_conductivity.append(b)
        b_conductivity = [complex(0, b) for b in b_conductivity]
        b_conductivity = numpy.array(b_conductivity)
        b_conductivity = numpy.diag(b_conductivity)
        y_matrix = y_matrix + b_conductivity
        return y_matrix

    @staticmethod
    def get_incident_matrix() -> numpy.ndarray:
        """
        Получение матрицы инцидентности
        :return: матрица инцидентности
        """
        incident_matrix = numpy.zeros((len(GV.nodes), len(GV.branches)))
        for i, branch in enumerate(GV.branches):
            number_node = [None, None]
            for j, node in enumerate(GV.nodes):
                if branch.node_s == node.name:
                    number_node[0] = j
                elif branch.node_e == node.name:
                    number_node[1] = j
                else:
                    continue
            incident_matrix[number_node[0], i] = 1
            incident_matrix[number_node[1], i] = -1
        return incident_matrix

    @staticmethod
    def get_imbalances_s(y_matrix: numpy.ndarray) -> list:
        """
        Получение небалансов полной мощности узлов
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
            p1 = -s_power.real
            p2 = -y_matrix[i, i].real * abs(GV.nodes[i].voltage) ** 2
            p3 = 0
            p4 = 0
            q1 = -s_power.imag
            q2 = y_matrix[i, i].imag * abs(GV.nodes[i].voltage) ** 2
            q3 = 0
            q4 = 0
            for j in range(node_count):
                if j != i:
                    p3 += y_matrix[i, j].real * GV.nodes[j].voltage.real + y_matrix[i, j].imag * GV.nodes[
                        j].voltage.imag
                    p4 += -y_matrix[i, j].imag * GV.nodes[j].voltage.real + y_matrix[i, j].real * GV.nodes[
                        j].voltage.imag
                    q3 += -y_matrix[i, j].imag * GV.nodes[j].voltage.real + y_matrix[i, j].real * GV.nodes[
                        j].voltage.imag
                    q4 += y_matrix[i, j].imag * GV.nodes[j].voltage.imag + y_matrix[i, j].real * GV.nodes[
                        j].voltage.real
            p3 = - GV.nodes[i].voltage.real * p3
            p4 = - GV.nodes[i].voltage.imag * p4
            q3 = - GV.nodes[i].voltage.real * q3
            q4 = GV.nodes[i].voltage.imag * q4
            imbalances_s.append(complex(p1 + p2 + p3 + p4, q1 + q2 + q3 + q4))
        return imbalances_s

    @staticmethod
    def unbalance_condition(imbalances_s: list) -> bool:
        """
        Проверка, что все небалансы меньше заданной точности
        :param imbalances_s: список небалансов полной мощности узлов
        :return: False, если точность не достигнута, иначе True
        """
        for i, imb_s in enumerate(imbalances_s):
            if GV.nodes[i].type_node != 'ИП':
                if abs(imb_s.real) > GV.OPTIONS.precision or abs(imb_s.imag) > GV.OPTIONS.precision:
                    return False
            else:
                continue
        return True


if __name__ == '__main__':
    pass
