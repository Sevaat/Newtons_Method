from src.model.newton_method.NewtonMethodClass import NewtonMethod
from src.calculation.ImbalancesClass import Imbalances
from src.calculation.JacobiMatrixClass import JacobiMatrix
from src.calculation.LinearAlgebraicEquationSolverClass import LinearAlgebraicEquationSolver
from src.calculation.VoltageCorrectionClass import VoltageCorrection


class NewtonMethodBuilder:
    def __init__(self, newton_method = NewtonMethod()):
        self.newton_method = newton_method

    @property
    def cartesian_or_polar(self):
        return CartesianOrPolarBuilder(self.newton_method)

    def build(self):
        return self.newton_method

class CartesianOrPolarBuilder(NewtonMethodBuilder):

    def __init__(self, newton_method):
        super().__init__(newton_method)

    def set_cartesian_or_polar(self, cartesian_or_polar):
        if cartesian_or_polar == 'cartesian':
            self.newton_method.imbalance_calculation = Imbalances.get_imbalances_s_cartesian
            self.newton_method.jacoby_matrix_calculation = JacobiMatrix.get_jacobi_matrix_cartesian
            self.newton_method.linear_algebraic_equation_solver = LinearAlgebraicEquationSolver.l_a_e_s_cartesian
            self.newton_method.voltage_correction = VoltageCorrection.voltage_correction_cartesian
        elif cartesian_or_polar == 'polar':
            self.newton_method.imbalance_calculation = Imbalances.get_imbalances_s_polar
            self.newton_method.jacoby_matrix_calculation = JacobiMatrix.get_jacobi_matrix_polar
            self.newton_method.linear_algebraic_equation_solver = LinearAlgebraicEquationSolver.l_a_e_s_polar
            self.newton_method.voltage_correction = VoltageCorrection.voltage_correction_polar
        else:
            self.newton_method.imbalance_calculation = None
            self.newton_method.jacoby_matrix_calculation = None
            self.newton_method.linear_algebraic_equation_solver = None
            self.newton_method.voltage_correction = None
        return self


if __name__ == '__main__':
    pass
