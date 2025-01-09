import unittest
from src.utils.FileManagerClass import FileManager
import src.utils.GlobalVariables as GV
from src.calculation.ImbalancesClass import Imbalances
from src.calculation.JacobiMatrixClass import JacobiMatrix
from src.calculation.LinearAlgebraicEquationSolverClass import LinearAlgebraicEquationSolver
from src.calculation.VoltageCorrectionClass import VoltageCorrection
from src.calculation.UnbalanceConditionClass import UnbalanceCondition

filepath = "../data_tests/Data_Test_1.txt"


class FileManagerClassTests(unittest.TestCase):
    def test_get_options_cartesian(self):
        options = FileManager._FileManager__get_options(filepath)

        result = [options.nominal_voltage, options.precision, options.number_of_iterations, options.type]

        self.assertEqual(result, [110, 0.001, 100, 'cartesian'])

    def test_get_nodes(self):
        GV.OPTIONS = FileManager._FileManager__get_options(filepath)
        GV.nodes = FileManager._FileManager__get_nodes(filepath)

        result = [
            GV.nodes[0].s_power, GV.nodes[0].voltage, GV.nodes[0].type_node, GV.nodes[0].name,
            GV.nodes[1].s_power, GV.nodes[1].voltage, GV.nodes[1].type_node, GV.nodes[1].name,
            GV.nodes[2].s_power, GV.nodes[2].voltage, GV.nodes[2].type_node, GV.nodes[2].name
        ]

        expected_result = [
            complex(float('inf'), float('inf')), complex(110 * 1.1,0.0), 'ИП', '0',
            complex(28.8675, 17.3205), complex(110.0,0.0), 'ИОМ', '1',
            complex(46.1880, 23.0940), complex(110.0,0.0), 'Н', '2'
        ]

        self.assertEqual(result, expected_result)

    def test_get_branch(self):
        GV.branches = FileManager._FileManager__get_branches(filepath)

        result = [
            GV.branches[0].node_s, GV.branches[0].node_e, GV.branches[0].z_resistance, GV.branches[0].b_conductivity,
            GV.branches[1].node_s, GV.branches[1].node_e, GV.branches[1].z_resistance, GV.branches[1].b_conductivity,
            GV.branches[2].node_s, GV.branches[2].node_e, GV.branches[2].z_resistance, GV.branches[2].b_conductivity
        ]

        expected_result = [
            '0', '1', complex(10, 20), 0,
            '0', '2', complex(15, 30), 0,
            '1', '2', complex(10, 25), 0,
        ]

        self.assertEqual(result, expected_result)

    def test_get_newton_method(self):
        GV.NEWTONMETHOD = FileManager._FileManager__get_newton_method(filepath)

        result = [
            GV.NEWTONMETHOD.voltage_correction,
            GV.NEWTONMETHOD.linear_algebraic_equation_solver,
            GV.NEWTONMETHOD.unbalance_condition,
            GV.NEWTONMETHOD.imbalance_calculation,
            GV.NEWTONMETHOD.jacoby_matrix_calculation
        ]

        expected_result = [
            VoltageCorrection.voltage_correction_cartesian,
            LinearAlgebraicEquationSolver.l_a_e_s_cartesian,
            UnbalanceCondition.unbalance_condition,
            Imbalances.get_imbalances_s_cartesian,
            JacobiMatrix.get_jacobi_matrix_cartesian
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()