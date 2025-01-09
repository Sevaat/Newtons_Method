import unittest

from src.utils.FileManagerClass import FileManager
import src.GlobalVariables as GV

filepath = "../data_tests/Data_Test_1.txt"


class FileManagerClassTests(unittest.TestCase):

    def test_get_options(self):
        options = FileManager._FileManager__get_options(filepath)

        result = [options.nominal_voltage, options.precision, options.number_of_iterations]

        self.assertEqual(result, [110, 0.001, 100])

    def test_get_nodes(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)

        result = [
            nodes[0].s_power, nodes[0].voltage, nodes[0].type_node, nodes[0].name,
            nodes[1].s_power, nodes[1].voltage, nodes[1].type_node, nodes[1].name,
            nodes[2].s_power, nodes[2].voltage, nodes[2].type_node, nodes[2].name
        ]

        expected_result = [
            complex(float('inf'), float('inf')), complex(110 * 1.1,0.0), 'ИП', '0',
            complex(28.8675, 17.3205), complex(110.0,0.0), 'ИОМ', '1',
            complex(46.1880, 23.0940), complex(110.0,0.0), 'Н', '2'
        ]

        self.assertEqual(result, expected_result)

    def test_get_branch(self):
        options = FileManager._FileManager__get_options(filepath)
        GV.OPTIONS = options
        nodes = FileManager._FileManager__get_nodes(filepath)
        GV.nodes = nodes
        branches = FileManager._FileManager__get_branches(filepath)

        result = [
            branches[0].node_s, branches[0].node_e, branches[0].z_resistance, branches[0].b_conductivity,
            branches[1].node_s, branches[1].node_e, branches[1].z_resistance, branches[1].b_conductivity,
            branches[2].node_s, branches[2].node_e, branches[2].z_resistance, branches[2].b_conductivity,
        ]

        expected_result = [
            '0', '1', complex(10, 20), 0,
            '0', '2', complex(15, 30), 0,
            '1', '2', complex(10, 25), 0,
        ]

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()