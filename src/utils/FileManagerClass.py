from abc import ABC
from tkinter import filedialog
from src.model.OptionsClass import Options
import src.GlobalVariables as GV
from src.model.NodeClass import Node
from src.model.BranchClass import Branch


class FileManager(ABC):
    @staticmethod
    def save_file():
        filepath = filedialog.asksaveasfilename(
            title='Сохранение файла',
            defaultextension='txt',
            initialfile='Result.txt'
        )
        if filepath != "":
            with open(filepath, "w") as file:
                for node in GV.nodes:
                    file.write(str(node))

    @staticmethod
    def open_file():
        filepath = filedialog.askopenfilename(
            title='Загрузка файла',
            defaultextension='txt',
            initialfile='Data.txt'
        )
        if filepath != "":
            GV.OPTIONS = FileManager.__get_options(filepath)
            GV.nodes = FileManager.__get_nodes(filepath)
            GV.branches = FileManager.__get_branch(filepath)

    @staticmethod
    def __get_options(filepath) -> Options:
        with open(filepath, "r") as file:
            options = Options()
            for line in file:
                data_line = line.strip().split(':')
                if data_line[0] == 'Номинальное напряжение сети, кВ':
                    options.nominal_voltage = int(data_line[1].strip())
                elif data_line[0] == 'Точность расчета':
                    options.precision = float(data_line[1].strip())
                elif data_line[0] == 'Количество итераций МН':
                    options.number_of_iterations = int(data_line[1].strip())
                else:
                    continue
            return options

    @staticmethod
    def __get_nodes(filepath) -> [Node]:
        with open(filepath, "r") as file:
            nodes = []
            for line in file:
                data_line = line.strip().split(':')
                if data_line[0] == 'Узел (имя, P, Q, тип)':
                    data_node = data_line[1].strip().split('/')
                    node = Node()
                    node.name = data_node[0]
                    node.s_power = complex(float(data_node[1]), float(data_node[2]))
                    node.type_node = data_node[3]
                    if node.type_node == "ИП":
                        node.voltage = complex(GV.OPTIONS.nominal_voltage * 1.1, 0)
                    else:
                        node.voltage = complex(GV.OPTIONS.nominal_voltage, 0)
                    nodes.append(node)
                else:
                    continue
            return nodes

    @staticmethod
    def __get_branch(filepath) -> [Branch]:
        with open(filepath, "r") as file:
            branches = []
            for line in file:
                data_line = line.strip().split(':')
                if data_line[0] == 'Ветвь (начало, конец, R, X, B)':
                    data_branch = data_line[1].strip().split('/')
                    branch = Branch()
                    branch.node_s = data_branch[0]
                    branch.node_e = data_branch[1]
                    branch.z_resistance = complex(float(data_branch[2]), float(data_branch[3]))
                    branch.b_conductivity = float(data_branch[4])
                    branches.append(branch)
                else:
                    continue
            return branches


if __name__ == '__main__':
    pass
