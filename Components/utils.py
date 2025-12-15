import pandas as pd
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTableWidget


class InputBox(QWidget):
    def __init__(self, label_text="Enter txt: "):
        super().__init__()
        self.label = QLabel(label_text)
        self.input = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        self.setLayout(layout)

class UploadBox(QWidget):
    def __init__(self):
        super().__init__()
        self.upload_label = QLabel("Upload Files:")
        self.file_type_label = QLabel("Please upload .xls, .xlsx or CSV files ONLY")
        self.icons = []

        icon_paths = ['Icons/img.png', 'Icons/img_1.png', 'Icons/img_2.png']

        picmaps = []

        for path in icon_paths:
            pic_label = QLabel()
            pixmap = QPixmap(path).scaled(75, 75, aspectRatioMode=Qt.AspectRatioMode.IgnoreAspectRatio,
                                          transformMode=Qt.TransformationMode.SmoothTransformation)
            picmaps.append(pixmap)
            pic_label.setPixmap(pixmap)
            self.icons.append(pic_label)

        layout = QHBoxLayout()
        layout.addWidget(self.upload_label)
        for icon in self.icons:
            layout.addWidget(icon)

        self.setLayout(layout)


class Button(QWidget):
    def __init__(self, callable=None):
        super().__init__()

        layout = QHBoxLayout()

        self.button = QPushButton("Upload Files")
        self.button.setMaximumSize(QSize(200, 100))
        if callable:
            self.button.clicked.connect(callable)
        else:
            self.button.clicked.connect(self.on_click)
        self.setMinimumSize(QSize(400, 300))

        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_click(self):
        print("CLICKED")
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(600, 400))

    def load_excel(self, path, sheet):
        file = pd.read_excel(path, sheet_name=sheet)
        file.fillna('', inplace=True)
        self.setRowCount(file.shape[0])
        self.setColumnCount(file.shape[1])
        self.setHorizontalHeaderLabels(file.columns.tolist())

