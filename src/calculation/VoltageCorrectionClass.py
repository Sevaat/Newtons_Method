from abc import ABC
import src.utils.GlobalVariables as GV


class VoltageCorrection(ABC):
    @staticmethod
    def voltage_correction_cartesian(delta_voltage):
        """
        Корректировка напряжений узлов в декартовых координатах
        :param delta_voltage: корректировки напряжений узлов
        :return: скорректированные напряжения узлов
        """
        j = 0
        for i in range(len(GV.nodes)):
            if GV.nodes[i].type_node != 'ИП':
                GV.nodes[i].voltage = GV.nodes[i].voltage + delta_voltage[j]
                j += 1

    @staticmethod
    def voltage_correction_polar(delta_voltage):
        """
        Корректировка напряжений узлов в полярных координатах
        :param delta_voltage: корректировки напряжений узлов
        :return: скорректированные напряжения узлов
        """
        j = 0
        for i in range(len(GV.nodes)):
            if GV.nodes[i].type_node != 'ИП':
                voltage = GV.nodes[i].get_polar_voltage() + delta_voltage[j][0]
                angle = GV.nodes[i].get_polar_angle() + delta_voltage[j][1]
                GV.nodes[i].polar_to_cartesian(voltage, angle)
                j += 1