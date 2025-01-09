import unittest
import numpy
from src.utils.FileManagerClass import FileManager
import src.GlobalVariables as GV
from src.calculation.ModeCalculationDataClass import ModeCalculationData as MCD

filepath = "../data_tests/Data_Test_1.txt"


class ModelCalculationDataClassTests(unittest.TestCase):

    def test_get_incident_matrix(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        i_m = MCD.get_incident_matrix()

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
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = numpy.round(MCD.get_y_matrix(), 3)

        result = [
            [y_m[0][0], y_m[0][1], y_m[0][2]],
            [y_m[1][0], y_m[1][1], y_m[1][2]],
            [y_m[2][0], y_m[2][1], y_m[2][2]]
        ]

        expected_result = [
            [complex(0.033, -0.067), complex(-0.020, 0.040), complex(-0.013, 0.027)],
            [complex(-0.020, 0.040), complex(0.034, -0.074), complex(-0.014, 0.034)],
            [complex(-0.013, 0.027), complex(-0.014, 0.034), complex(0.027, -0.061)]
        ]

        self.assertEqual(result, expected_result)

    def test_get_imbalances_s(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = MCD.get_y_matrix()
        imbalances_s = MCD.get_imbalances_s(y_m)

        result = [complex(round(x.real, 3), round(x.imag, 3)) for x in imbalances_s]

        expected_result = [complex(39.868, 39.321), complex(-38.855, -8.427)]

        self.assertEqual(result[1:], expected_result)

    def test_unbalance_condition_1(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = MCD.get_y_matrix()
        imbalances_s = MCD.get_imbalances_s(y_m)
        result = MCD.unbalance_condition(imbalances_s)

        self.assertEqual(result, False)

    def test_unbalance_condition_2(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        imbalances_s = [complex(0.0001, 0.0001), complex(0.0001, 0.0001)]
        result = MCD.unbalance_condition(imbalances_s)

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()