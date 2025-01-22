import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix
from src.NewtonMethod import newton_method
from math import *

filepath_1 = "data_tests/Data_Test_1.txt"
filepath_2 = "data_tests/Data_Test_2.txt"


class NewtonMethodTests(unittest.TestCase):
    def test_newton_method_cartesian(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_1)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_1)
        GV.branches = FileManager._FileManager__get_branches(filepath_1)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_1)

        newton_method()

        result = [round(abs(GV.nodes[1].voltage), 3), round(abs(GV.nodes[2].voltage), 3)]

        expected_result = [115.916, 110.249]

        self.assertEqual(result, expected_result)

    def test_newton_method_polar(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_2)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_2)
        GV.branches = FileManager._FileManager__get_branches(filepath_2)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_2)

        newton_method()

        result = [round(abs(GV.nodes[1].voltage), 3), round(abs(GV.nodes[2].voltage), 3)]

        expected_result = [115.92, 110.245]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()