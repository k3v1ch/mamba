import sys
from PyQt5 import QtWidgets, uic

class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calc.ui", self)

        self.expression = ""
        

        self.findChild(QtWidgets.QPushButton, "pushButton_0").clicked.connect(lambda: self.add_to_expression("0"))
        self.findChild(QtWidgets.QPushButton, "pushButton_1").clicked.connect(lambda: self.add_to_expression("1"))
        self.findChild(QtWidgets.QPushButton, "pushButton_2").clicked.connect(lambda: self.add_to_expression("2"))
        self.findChild(QtWidgets.QPushButton, "pushButton_3").clicked.connect(lambda: self.add_to_expression("3"))
        self.findChild(QtWidgets.QPushButton, "pushButton_4").clicked.connect(lambda: self.add_to_expression("4"))
        self.findChild(QtWidgets.QPushButton, "pushButton_5").clicked.connect(lambda: self.add_to_expression("5"))
        self.findChild(QtWidgets.QPushButton, "pushButton_6").clicked.connect(lambda: self.add_to_expression("6"))
        self.findChild(QtWidgets.QPushButton, "pushButton_7").clicked.connect(lambda: self.add_to_expression("7"))
        self.findChild(QtWidgets.QPushButton, "pushButton_8").clicked.connect(lambda: self.add_to_expression("8"))
        self.findChild(QtWidgets.QPushButton, "pushButton_9").clicked.connect(lambda: self.add_to_expression("9"))


        self.findChild(QtWidgets.QPushButton, "pbAdd").clicked.connect(lambda: self.add_to_expression("+"))
        self.findChild(QtWidgets.QPushButton, "pbSubt").clicked.connect(lambda: self.add_to_expression("-"))
        self.findChild(QtWidgets.QPushButton, "pbMult").clicked.connect(lambda: self.add_to_expression("*"))
        self.findChild(QtWidgets.QPushButton, "pbDiv").clicked.connect(lambda: self.add_to_expression("/"))
        self.findChild(QtWidgets.QPushButton, "pbPow2").clicked.connect(lambda: self.add_to_expression("**"))


        self.findChild(QtWidgets.QPushButton, "pbEqual").clicked.connect(self.evaluate)

        self.findChild(QtWidgets.QPushButton, "pbClear").clicked.connect(self.clear)

    def add_to_expression(self, val):
        self.expression += val
        self.update_lcd()

    def update_lcd(self):
        try:
            result = eval(self.expression)
            self.lcdNumber.display(result)
        except:
            self.lcdNumber.display(0)

    def evaluate(self):
        try:
            result = eval(self.expression)
            self.lcdNumber.display(result)
            self.expression = str(result)
        except:
            self.lcdNumber.display("lcdNumber")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.lcdNumber.display(0)

if  __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())