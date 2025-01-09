import unittest
import numpy
from src.utils.FileManagerClass import FileManager
import src.GlobalVariables as GV
from src.calculation.ModeCalculationDataClass import ModeCalculationData as MCD
from src.calculation.NewtonCalculation import NewtonClass as NC

filepath = "../data_tests/Data_Test_1.txt"


class NewtonCalculationTests(unittest.TestCase):

    def test_get_jacobi_matrix(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = MCD.get_y_matrix()
        j_m = numpy.round(NC.get_jacobi_matrix(y_m), 3)

        result = [
            [j_m[0][0], j_m[0][1], j_m[0][2], j_m[0][3]],
            [j_m[1][0], j_m[1][1], j_m[1][2], j_m[1][3]],
            [j_m[2][0], j_m[2][1], j_m[2][2], j_m[2][3]],
            [j_m[3][0], j_m[3][1], j_m[3][2], j_m[3][3]]
        ]

        expected_result = [
            [-3.617, 8.393, 1.517, -3.793],
            [-7.993, -3.817, 3.793, 1.517],
            [1.517, -3.793, -2.917, 6.860],
            [3.793, 1.517, -6.593, -3.051]
        ]

        self.assertEqual(result, expected_result)

    def test_linear_algebraic_equation_solver(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = MCD.get_y_matrix()
        i_s = MCD.get_imbalances_s(y_m)
        j_m = NC.get_jacobi_matrix(y_m)

        result = NC.linear_algebraic_equation_solver(i_s, j_m)
        result = [complex(round(r.real, 3), round(r.imag, 3)) for r in result]

        expected_result = [complex(5.915, -0.308), complex(0.098, 4.227)]

        self.assertEqual(result, expected_result)

    def test_voltage_correction(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        nodes[0].voltage = complex(115, 0)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)
        GV.branches = branches

        y_m = MCD.get_y_matrix()
        i_s = MCD.get_imbalances_s(y_m)
        j_m = NC.get_jacobi_matrix(y_m)
        d_v = NC.linear_algebraic_equation_solver(i_s, j_m)
        NC.voltage_correction(d_v)

        result = [GV.nodes[1].voltage, GV.nodes[2].voltage]
        result = [complex(round(r.real, 3), round(r.imag, 3)) for r in result]

        expected_result = [complex(115.915, -0.308), complex(110.098, 4.227)]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()