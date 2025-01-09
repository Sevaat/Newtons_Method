from abc import ABC
import numpy
import src.utils.GlobalVariables as GV


class YMatrix(ABC):
    @staticmethod
    def get_y_matrix() -> numpy.ndarray:
        """
        Получение матрицы собственных и взаимных проводимостей узлов
        :return: матрица собственных и взаимных проводимостей узлов
        """
        y_matrix = numpy.array([1 / branch.z_resistance for branch in GV.branches])
        incident_matrix = YMatrix.get_incident_matrix()
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