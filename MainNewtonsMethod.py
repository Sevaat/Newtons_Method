from src.calculation.NewtonCalculation import NewtonClass
from src.utils.FileManagerClass import FileManager


def main():
    FileManager.open_file()
    NewtonClass.calculation()
    FileManager.save_file()


if __name__ == '__main__':
    main()
