from src.NewtonMethod import newton_method
from src.utils.FileManagerClass import FileManager


def main():
    FileManager.open_file()
    newton_method()
    FileManager.save_file()


if __name__ == '__main__':
    main()
