import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath_1 = "../data_tests/Data_Test_1.txt"
filepath_2 = "../data_tests/Data_Test_2.txt"


class LinearAlgebraicEquationSolverClassTests(unittest.TestCase):
    def test_linear_algebraic_equation_solver_cartesian(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_1)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_1)
        GV.branches = FileManager._FileManager__get_branches(filepath_1)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_1)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        i_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)
        j_m = GV.NEWTONMETHOD.jacoby_matrix_calculation(y_m)

        result = GV.NEWTONMETHOD.linear_algebraic_equation_solver(i_s, j_m)
        result = [complex(round(r.real, 3), round(r.imag, 3)) for r in result]

        expected_result = [complex(5.915, 0.308), complex(0.098, -4.227)]

        self.assertEqual(result, expected_result)

    def test_linear_algebraic_equation_solver_polar(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath_2)
        GV.nodes = FileManager._FileManager__get_nodes(filepath_2)
        GV.branches = FileManager._FileManager__get_branches(filepath_2)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath_2)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        i_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)
        j_m = GV.NEWTONMETHOD.jacoby_matrix_calculation(y_m)

        result = GV.NEWTONMETHOD.linear_algebraic_equation_solver(i_s, j_m)
        result = [[round(r[0], 3), round(r[1], 3)] for r in result]

        expected_result = [[5.915, 0.003], [0.098, -0.038]]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
