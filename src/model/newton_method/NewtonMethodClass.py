from src.calculation.UnbalanceConditionClass import UnbalanceCondition


class NewtonMethod:
    def __init__(self):
        # тип расчета небаланса: cartesian или polar
        self.imbalance_calculation = None
        self.unbalance_condition = UnbalanceCondition.unbalance_condition
        self.jacoby_matrix_calculation = None
        self.linear_algebraic_equation_solver = None
        self.voltage_correction = None


if __name__ == '__main__':
    pass
