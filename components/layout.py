from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QFrame

from components.header import Header
from components.form import Form


class Layout:
    def __init__(self, direction):
        self.direction = direction

    def display(self) -> QHBoxLayout | QVBoxLayout:
        if self.direction == "H":
            layout = QHBoxLayout()
        elif self.direction == "V":
            layout = QVBoxLayout()
        
        f1 = Header()
        f2 = Form()
        f3 = QFrame()
        f3.setStyleSheet("background: #ffff80")
        f3.setMinimumHeight(200)
        layout.addWidget(f1)
        layout.addWidget(f2)
        layout.addWidget(f3)
        return layout