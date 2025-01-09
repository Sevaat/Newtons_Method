from abc import ABC
import src.utils.GlobalVariables as GV


class UnbalanceCondition(ABC):
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
