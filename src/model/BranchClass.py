class Branch:
    def __init__(self):
        self.node_s = None # узел начала ветви
        self.node_e = None # узел конца ветви
        self.z_resistance = None # полное сопротивление ветви
        self.b_conductivity = None # емкостная проводимость

    def __str__(self):
        return f'''Ветвь соединяет узлы: {self.node_s} и {self.node_e}
Полное сопротивление ветви: {self.z_resistance} Ом
Емкостная проводимость ветви: {self.b_conductivity} См

'''

    def __repr__(self):
        return f'''Ветвь соединяет узлы: {self.node_s} и {self.node_e}
Полное сопротивление ветви: {self.z_resistance} Ом
Емкостная проводимость ветви: {self.b_conductivity} См

'''


if __name__ == '__main__':
    pass
