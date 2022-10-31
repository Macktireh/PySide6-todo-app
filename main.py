import sys

from PySide6 import QtGui as QtG
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame

from config.settings import staticFiles
from components.layout import Layout
from components.header import Header


class Button:
    def __init__(self):
        pass

    @staticmethod
    def display() -> QWidget:
        button = QPushButton()
        # button.setStyleSheet("background: #80ffff")
        return button






class BodyWidget:
    def __init__(self):
        pass

    @staticmethod
    def display() -> QWidget:
        widget = QWidget()
        widget.setStyleSheet("background: #f1f1f1")
        widget.setLayout(Layout(direction="V").display())
        return widget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.setWindowIcon(QtG.QIcon(staticFiles("img", "WML.png")))
        self.setMinimumSize(500, 400)
        # self.resize(1300, 700)
        # self.showMaximized()

        self.setCentralWidget(BodyWidget.display())

        statusBar = self.statusBar()
        statusBar.setStyleSheet("background: #F2F2F2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
