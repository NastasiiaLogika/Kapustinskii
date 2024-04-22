import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPixmap

class ApplicationConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Converter")
        self.setGeometry(100, 100, 500, 500)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.central_widget.setStyleSheet("backgroubd-color: #ffffff")

        self.label_converter = QLabel("З валюти", self)
        self.layout.addWidget(self.label_converter)

        self.converter_combo = QComboBox(self)
        self.converter_combo.addItem(["Долар", "Євро", "Гривня",])

app = QApplication(sys.argv)
window = ApplicationConverter()
window.show()
sys.exit(app.exec_())
