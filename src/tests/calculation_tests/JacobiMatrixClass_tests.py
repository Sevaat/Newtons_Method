import unittest
import numpy
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath_1 = "../data_tests/Data_Test_1.txt"
filepath_2 = "../data_tests/Data_Test_2.txt"


class JacobiMatrixClassTests(unittest.TestCase):
    def test_get_jacobi_matrix_cartesian(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_1)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_1)
        GV.branches = FileManager._FileManager__get_branches(filepath_1)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_1)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        j_m = numpy.round(GV.NEWTONMETHOD.jacoby_matrix_calculation(y_m), 3)

        result = [
            [j_m[0][0], j_m[0][1], j_m[0][2], j_m[0][3]],
            [j_m[1][0], j_m[1][1], j_m[1][2], j_m[1][3]],
            [j_m[2][0], j_m[2][1], j_m[2][2], j_m[2][3]],
            [j_m[3][0], j_m[3][1], j_m[3][2], j_m[3][3]]
        ]

        expected_result = [
            [3.617, 8.393, -1.517, -3.793],
            [7.993, -3.817, -3.793, 1.517],
            [-1.517, -3.793, 2.917, 6.860],
            [-3.793, 1.517, 6.593, -3.051]
        ]

        self.assertEqual(result, expected_result)

    def test_get_jacobi_matrix_polar(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_2)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_2)
        GV.branches = FileManager._FileManager__get_branches(filepath_2)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_2)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        j_m = numpy.round(GV.NEWTONMETHOD.jacoby_matrix_calculation(y_m), 3)

        result = [
            [j_m[0][0], j_m[0][1], j_m[0][2], j_m[0][3]],
            [j_m[1][0], j_m[1][1], j_m[1][2], j_m[1][3]],
            [j_m[2][0], j_m[2][1], j_m[2][2], j_m[2][3]],
            [j_m[3][0], j_m[3][1], j_m[3][2], j_m[3][3]]
        ]

        expected_result = [
            [3.617, 923.241, -1.517, -417.241],
            [7.993, -419.897, -3.793, 166.897],
            [-1.517, -417.241, 2.917, 754.575],
            [-3.793, 166.897, 6.593, -335.563]
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
