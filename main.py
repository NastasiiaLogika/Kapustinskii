import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Конвертер валют') 
        self.setWindowIcon(QIcon('exchanging.png'))
        self.ui.input_currency.setPlaceholderText('З валюти:')
        self.ui.input_amount.setPlaceholderText('В мене є:')
        self.ui.output_currency.setPlaceholderText('В валюту:')
        self.ui.output_amount.setPlaceholderText('Я отримаю:')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())
        if output_currency == "UAH" and input_currency == "USD":
            output_amount = round((input_amount*39.54), 2)
        elif output_currency == "UAH" and input_currency == "PLN":
            output_amount = round((input_amount*9.90), 2)
        elif output_currency == "UAH" and input_currency == "EUR":
            output_amount = round((input_amount*42.66), 2)
        else:
            output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())


