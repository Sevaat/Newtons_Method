from abc import ABC
import src.utils.GlobalVariables as GV


class VoltageCorrection(ABC):
    @staticmethod
    def voltage_correction_cartesian(delta_voltage):
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