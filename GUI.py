from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QPixmapCache, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QMenu


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")


        #does it have to be above the layout and container???
        #or can it be below, along with the addwidget fn?
        self.label = QLabel()
        self.icons = []

        icon_paths = ['./Icons/img.png', './Icons/img_1.png', './Icons/img_2.png']

        picmaps = []

        for path in icon_paths:
            pic_label = QLabel()
            pixmap = QPixmap(path).scaled(75, 75, aspectRatioMode=Qt.AspectRatioMode.IgnoreAspectRatio,
                    transformMode=Qt.TransformationMode.SmoothTransformation)
            picmaps.append(pixmap)
            pic_label.setPixmap(pixmap)
            self.icons.append(pic_label)

        self.input = QLineEdit()


        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        for icon in self.icons:
            layout.addWidget(icon)

        container = QWidget()
        container.setLayout(layout)


        self.button = QPushButton("Upload Files")
        self.button.setMaximumSize(QSize(200, 100))
        self.button.clicked.connect(self.on_click)
        self.setMinimumSize(QSize(400, 300))

        layout.addWidget(self.button)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def on_click(self):
        print("CLICKED")
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        self.label.setText(self.input.text())


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
