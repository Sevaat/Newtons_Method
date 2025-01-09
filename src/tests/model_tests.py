import unittest
from src.model.NodeClass import Node
import math

filepath = "data_tests/Data_Test_1.txt"


class NodeClassTests(unittest.TestCase):
    def test_get_polar_voltage(self):
        node = Node()
        node.voltage = complex(115, 115)

        result = node.get_polar_voltage()

        expected_result = (abs(node.voltage), math.pi / 4)

        self.assertEqual(result, expected_result)

    def test_polar_to_cartesian(self):
        node = Node()
        node.voltage = complex(0, 0)

        node.polar_to_cartesian((115**2 + 115**2)**0.5, math.pi / 4)
        node.voltage = complex(round(node.voltage.real, 0), round(node.voltage.imag, 0))

        result = node.voltage

        expected_result = complex(115, 115)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()