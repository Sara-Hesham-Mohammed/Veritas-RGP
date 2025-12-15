from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QPixmapCache, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QMenu, \
    QHBoxLayout, QTableWidget
from Components.Footer import Footer
from Components.utils import InputBox, UploadBox, Button, Table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.input = InputBox("Second Input: ")
        self.upload_box = UploadBox()
        self.table = Table()
        self.button = Button(self.table.load_excel("Kayan.xlsx","ImportEntriesTemplate"))

        self.footer = Footer()



        main_layout = QVBoxLayout()
        main_layout.addWidget(self.input)
        main_layout.addWidget(self.upload_box)
        main_layout.addWidget(self.button)
        main_layout.addWidget(self.footer)
        main_layout.addWidget(self.table)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
