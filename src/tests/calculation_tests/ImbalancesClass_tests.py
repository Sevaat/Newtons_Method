import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath_1 = "../data_tests/Data_Test_1.txt"
filepath_2 = "../data_tests/Data_Test_2.txt"



class ImbalancesClassTests(unittest.TestCase):
    def test_get_imbalances_s_cartesian(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_1)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_1)
        GV.branches = FileManager._FileManager__get_branches(filepath_1)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_1)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        imbalances_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)

        result = [complex(round(x.real, 3), round(x.imag, 3)) for x in imbalances_s]

        expected_result = [complex(-39.868, -39.321), complex(38.855, 8.427)]

        self.assertEqual(result[1:], expected_result)

    def test_get_imbalances_s_polar(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_2)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_2)
        GV.branches = FileManager._FileManager__get_branches(filepath_2)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_2)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        imbalances_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)

        result = [complex(round(x.real, 4), round(x.imag, 4)) for x in imbalances_s]

        expected_result = [complex(-39.8675, -39.3205), complex(38.8547, 8.4273)]

        self.assertEqual(result[1:], expected_result)


if __name__ == '__main__':
    unittest.main()