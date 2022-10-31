from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtCore import Qt


class Header(QFrame):
    def __init__(self) -> None:
        super(Header, self).__init__()
        self.setStyleSheet("background: #b1becd; text-align: center")
        self.setMinimumHeight(40)
        self.setMaximumHeight(50)
        
        labelTitle = QLabel("This is the title App")
        labelTitle.setAlignment(Qt.AlignCenter)
        labelTitle.setStyleSheet("font-size: 20px; font-family: monospace; font-weight: bold")
        
        boxLay = QVBoxLayout()
        boxLay.addWidget(labelTitle)
        
        self.setLayout(boxLay)

