from PySide6.QtWidgets import QPushButton, QLineEdit, QHBoxLayout, QFrame
from PySide6.QtCore import Qt


class Form(QFrame):

    def __init__(self) -> None:
        super(Form, self).__init__()
        self.setStyleSheet("background: #d0e3dd; text-align: center")
        self.setMinimumHeight(50)
        self.setMaximumHeight(70)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Entrer une tache")
        self.input.setMinimumHeight(30)
        self.input.setStyleSheet("font-size: 14px; color: #000; font-family: monospace")


        self.btn = QPushButton("Ajouter")
        self.btn.setMinimumHeight(30)
        self.btn.setMinimumWidth(100)
        self.btn.setStyleSheet("background: #8dd0f1")
        self.btn.clicked.connect(self.handleClick)

        box = QHBoxLayout()
        box.addWidget(self.input)
        box.addWidget(self.btn)

        self.setLayout(box)

    def handleClick(self):
        print(self.input.text())