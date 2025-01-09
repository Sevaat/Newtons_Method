import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.YMatrixClass import YMatrix

filepath = "../data_tests/Data_Test_1.txt"


class VoltageCorrectionClassTests(unittest.TestCase):
    def test_voltage_correction_cartesian(self):
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

        result = [GV.nodes[1].voltage, GV.nodes[2].voltage]
        result = [complex(round(r.real, 3), round(r.imag, 3)) for r in result]

        expected_result = [complex(115.915, -0.308), complex(110.098, 4.227)]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
