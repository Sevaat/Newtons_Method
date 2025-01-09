import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath = "../data_tests/Data_Test_1.txt"


class UnbalanceCorrectionClassTests(unittest.TestCase):
    def test_unbalance_condition_cartesian_1(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)
        GV.branches = FileManager._FileManager__get_branches(filepath)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        imbalances_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)
        result = GV.NEWTONMETHOD.unbalance_condition(imbalances_s)

        self.assertEqual(result, False)

    def test_unbalance_condition_cartesian_2(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)
        GV.branches = FileManager._FileManager__get_branches(filepath)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)
        GV.nodes[0].voltage = complex(115, 0)

        imbalances_s = [complex(0.0001, 0.0001), complex(0.0001, 0.0001)]
        result = GV.NEWTONMETHOD.unbalance_condition(imbalances_s)

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()