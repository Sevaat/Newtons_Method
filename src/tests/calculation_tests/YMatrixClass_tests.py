import unittest
import numpy
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath = "../data_tests/Data_Test_1.txt"


class YMatrixClassTests(unittest.TestCase):
    def test_get_incident_matrix(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)
        GV.branches = FileManager._FileManager__get_branches(filepath)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)

        i_m = YMatrix.get_incident_matrix()

        result = [
            [i_m[0][0], i_m[0][1], i_m[0][2]],
            [i_m[1][0], i_m[1][1], i_m[1][2]],
            [i_m[2][0], i_m[2][1], i_m[2][2]]
        ]

        expected_result = [
            [1, 1, 0],
            [-1, 0, 1],
            [0, -1, -1]
        ]

        self.assertEqual(result, expected_result)

    def test_get_y_matrix(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)
        GV.branches = FileManager._FileManager__get_branches(filepath)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)

        y_m = numpy.round(YMatrix.get_y_matrix(), 4)

        result = [
            [y_m[0][0], y_m[0][1], y_m[0][2]],
            [y_m[1][0], y_m[1][1], y_m[1][2]],
            [y_m[2][0], y_m[2][1], y_m[2][2]]
        ]

        expected_result = [
            [complex(0.0333, -0.0667), complex(-0.0200, 0.0400), complex(-0.0133, 0.0267)],
            [complex(-0.0200, 0.0400), complex(0.0338, -0.0745), complex(-0.0138, 0.0345)],
            [complex(-0.0133, 0.0267), complex(-0.0138, 0.0345), complex(0.0271, -0.0611)]
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
