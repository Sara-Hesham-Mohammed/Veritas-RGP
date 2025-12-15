from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel


class Footer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        self.setLayout(layout)
        label = QLabel("Footer")
        label.setStyleSheet("color: white;")
        layout.addWidget(label)
        self.setFixedHeight(100)
        self.setStyleSheet("background-color: #000080;")