import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix
from src.NewtonMethod import newton_method

filepath = "data_tests/Data_Test_1.txt"


class NewtonMethodTests(unittest.TestCase):
    def test_newton_method_cartesian(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)
        GV.branches = FileManager._FileManager__get_branches(filepath)
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)
        GV.nodes[0].voltage = complex(115, 0)

        y_m = YMatrix.get_y_matrix()
        i_s = GV.NEWTONMETHOD.imbalance_calculation(y_m)
        j_m = GV.NEWTONMETHOD.jacoby_matrix_calculation(y_m)
        d_v = GV.NEWTONMETHOD.linear_algebraic_equation_solver(i_s, j_m)
        GV.NEWTONMETHOD.voltage_correction(d_v)

        newton_method()

        result = [round(abs(GV.nodes[1].voltage), 3), round(abs(GV.nodes[2].voltage), 3)]

        expected_result = [115.415, 109.721]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()