import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator') # Set the GUI title
        self.setGeometry(292, 223, 400, 635) # Set the Geometry of the GUI ( x, y, width, height )
        # self.setWindowIcon(QIcon('File name')) Set an icon into the GUI

        self.numb = "0"
        self.algo = ""
        self.per = ""

        self.algorithms = QLabel(self)
        self.numbers = QLabel(self)
        self.button_0 = QPushButton("0", self)
        self.button_1 = QPushButton("1", self)
        self.button_2 = QPushButton("2", self)
        self.button_3 = QPushButton("3", self)
        self.button_4 = QPushButton("4", self)
        self.button_5 = QPushButton("5", self)
        self.button_6 = QPushButton("6", self)
        self.button_7 = QPushButton("7", self)
        self.button_8 = QPushButton("8", self)
        self.button_9 = QPushButton("9", self)

        self.numbers.setText(self.numb)

        self.bagi = QPushButton("÷", self)
        self.kali = QPushButton("×", self)
        self.kurang = QPushButton("-", self)
        self.tambah = QPushButton("+", self)

        self.sama_dengan = QPushButton("=", self)
        self.ce = QPushButton("CE", self)
        self.c = QPushButton("C", self)
        self.backspace = QPushButton("⌫", self)

        self.pangkat = QPushButton("x²", self)
        self.akar = QPushButton("²√x", self)
        self.koma = QPushButton(".", self)
        self.persen = QPushButton("%", self)
        self.satu_per_angka = QPushButton("⅟x", self)
        self.plus_minus = QPushButton("±", self)



        self.ui()
    def ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.algorithms.setGeometry(0, 0, 399, 25)
        self.numbers.setGeometry(0, 100, 398, 97)
        self.algorithms.setAlignment(Qt.AlignRight)
        self.numbers.setAlignment(Qt.AlignRight)

        grid = QGridLayout()

        grid.addWidget(self.algorithms, 0, 0, 0, 4)
        grid.addWidget(self.numbers, 1, 0, 1, 4)


        grid.addWidget(self.plus_minus, 7, 0)
        grid.addWidget(self.button_0, 7, 1)
        grid.addWidget(self.koma, 7, 2)
        grid.addWidget(self.sama_dengan, 7, 3)

        grid.addWidget(self.button_1, 6, 0)
        grid.addWidget(self.button_2, 6, 1)
        grid.addWidget(self.button_3, 6, 2)
        grid.addWidget(self.tambah, 6, 3)

        grid.addWidget(self.button_4, 5, 0)
        grid.addWidget(self.button_5, 5, 1)
        grid.addWidget(self.button_6, 5, 2)
        grid.addWidget(self.kurang, 5, 3)

        grid.addWidget(self.button_7, 4, 0)
        grid.addWidget(self.button_8, 4, 1)
        grid.addWidget(self.button_9, 4, 2)
        grid.addWidget(self.kali, 4, 3)

        grid.addWidget(self.satu_per_angka, 3, 0)
        grid.addWidget(self.pangkat, 3, 1)
        grid.addWidget(self.akar, 3, 2)
        grid.addWidget(self.bagi, 3, 3)

        grid.addWidget(self.persen, 2, 0)
        grid.addWidget(self.ce, 2, 1)
        grid.addWidget(self.c, 2, 2)
        grid.addWidget(self.backspace, 2, 3)

        grid.setSpacing(2)

        central_widget.setLayout(grid)

        self.algorithms.setObjectName("algorithms")
        self.numbers.setObjectName("numbers")

        self.button_0.setObjectName("numbers")
        self.button_1.setObjectName("numbers")
        self.button_2.setObjectName("numbers")
        self.button_3.setObjectName("numbers")
        self.button_4.setObjectName("numbers")
        self.button_5.setObjectName("numbers")
        self.button_6.setObjectName("numbers")
        self.button_7.setObjectName("numbers")
        self.button_8.setObjectName("numbers")
        self.button_9.setObjectName("numbers")
        self.koma.setObjectName("numbers")
        self.plus_minus.setObjectName("numbers")

        self.ce.setObjectName("fungsi_lain")
        self.c.setObjectName("fungsi_lain")
        self.backspace.setObjectName("operators")
        self.bagi.setObjectName("operators")
        self.kali.setObjectName("operators")
        self.kurang.setObjectName("operators")
        self.tambah.setObjectName("operators")
        self.pangkat.setObjectName("fungsi_lain")
        self.akar.setObjectName("fungsi_lain")
        self.persen.setObjectName("fungsi_lain")
        self.satu_per_angka.setObjectName("fungsi_lain")

        self.sama_dengan.setObjectName("sama_dengan")


        self.setStyleSheet("""
            QMainWindow{
                background-color:#202020;
            }
            QLabel{
                font-family:Segoe UI Variable;
                color:#ffffff;
            }
            QLabel#algorithms{
                font-size:15px;
                padding-top:65px;
            }
            QLabel#numbers{
                font-weight:bold;
                font-size:40px;
            }
            QPushButton{
                font-family:Segoe UI Variable;
                font-size:16px;
                border-radius:5px;
            }
            QPushButton#numbers{
                font-size:23px;
                font-weight:bold;
                padding:17px;
                background-color:#3b3b3b;
                color:#ffffff;
            }
            QPushButton#numbers:hover{
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#numbers:pressed{
                background-color:#282828;
                color:#ffffff;
            }
            QPushButton#operators{
                font-size:27px;
                padding:15px;
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#operators:hover{
                background-color:#3b3b3b;
                color:#ffffff;
            }
            QPushButton#operators:pressed{
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#fungsi_lain{
                font-size:16px;
                padding:23px;
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#fungsi_lain:hover{
                background-color:#3b3b3b;
                color:#ffffff;
            }
            QPushButton#fungsi_lain:pressed{
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#sama_dengan{
                font-size:27px;
                padding:15px;
                background-color:#76b9ed;
            }
            QPushButton#sama_dengan:hover{
                background-color:#6da9d8;
            }
            QPushButton#sama_dengan:pressed{
                background-color:#649ac3;
            }
            
            
        """)

        self.button_0.clicked.connect(lambda: self.angka("0"))
        self.button_1.clicked.connect(lambda: self.angka("1"))
        self.button_2.clicked.connect(lambda: self.angka("2"))
        self.button_3.clicked.connect(lambda: self.angka("3"))
        self.button_4.clicked.connect(lambda: self.angka("4"))
        self.button_5.clicked.connect(lambda: self.angka("5"))
        self.button_6.clicked.connect(lambda: self.angka("6"))
        self.button_7.clicked.connect(lambda: self.angka("7"))
        self.button_8.clicked.connect(lambda: self.angka("8"))
        self.button_9.clicked.connect(lambda: self.angka("9"))
        self.koma.clicked.connect(lambda: self.dot("."))

        self.bagi.clicked.connect(lambda: self.click_operator("/"))
        self.kali.clicked.connect(lambda: self.click_operator("*"))
        self.kurang.clicked.connect(lambda: self.click_operator("-"))
        self.tambah.clicked.connect(lambda: self.click_operator("+"))

        self.sama_dengan.clicked.connect(self.tombol_hasil)
        self.c.clicked.connect(self.c_button)
        self.ce.clicked.connect(self.ce_button)
        self.backspace.clicked.connect(self.backspace_button)
        self.plus_minus.clicked.connect(self.minus_plus)
        self.satu_per_angka.clicked.connect(self.satu_per_x)
        self.pangkat.clicked.connect(self.squared)
        self.akar.clicked.connect(self.square_root)
        self.persen.clicked.connect(self.percentage)

    def angka(self, num):
        if self.numb.startswith("0.") or "." in self.numb:
            self.numb += num
        elif self.numb == "0":
            self.numb = num
        else:
            self.numb = self.numb + num
        self.numbers.setText(self.numb)

    def click_operator(self, operator):
        try:
            if self.algo:
                if self.numb != "0":
                    self.algo += self.numb

                if self.algo[-1] in "+-*/":
                    self.algo = self.algo[:-1] + operator

                else:
                    self.algo = str(eval(self.algo)) + operator
            else:
                self.algo = self.numb + operator

            self.algorithms.setText(self.algo.replace("*", " × ").replace("/", " ÷ ").replace("-", " - ").replace("+", " + "))
            self.numb = "0"
            self.numbers.setText(self.numb)
        except ZeroDivisionError:
            self.numb = "0"
            self.algo = ""
            self.numbers.setText("Cant divide by Zero")
            self.algorithms.setText(self.algo.replace("*", " × ").replace("/", " ÷ ").replace("-", " - ").replace("+", " + "))

    def tombol_hasil(self):
        try:
            if self.numb != "0":
                if "/" or "-" or "+" or "*" in self.algo:
                    self.algo = self.algo + self.numb
                    hasil = str(eval(self.algo))
                    self.algorithms.setText(self.algo.replace("*", " × ").replace("/", " ÷ ").replace("-", " - ").replace("+", " + ") + " =")
                    self.numbers.setText(hasil)
                    self.algo = hasil
                    self.numb = ""
                elif "/" or "-" or "+" or "*" not in self.algo:
                    pass

            elif self.numb == "0" and " =" not in self.algorithms.text():
                self.algo = self.algo + self.numb
                hasil = str(eval(self.algo))
                self.algorithms.setText(
                    self.algo.replace("*", " × ").replace("/", " ÷ ").replace("-", " - ").replace("+", " + ") + " =")
                self.numbers.setText(str(hasil))
                self.numb = str(hasil)
                self.algo = hasil

            if self.numb == "0" and " =" in self.algorithms.text():
                pass
            else:
                pass

        except ZeroDivisionError:
            self.numb = "0"
            self.algo = ""
            self.numbers.setText("Cant divide by Zero")
            self.algorithms.setText(self.algo)

    def c_button(self):
        self.algo = ""
        self.numb = "0"
        self.numbers.setText(self.numb)
        self.algorithms.setText("")

    def ce_button(self):
        self.numb = "0"
        self.numbers.setText(self.numb)

    def backspace_button(self):
        self.numb = self.numb[:-1]
        if self.numb:
            self.numbers.setText(self.numb)
        else:
            self.numb = "0"
            self.numbers.setText(self.numb)

    def minus_plus(self):
        if self.numb == "0":
            pass
        elif self.numb[0] == "-":
            self.numb = self.numb[1:]
            self.numbers.setText(self.numb)
        else:
            self.numb = "-" + self.numb
            self.numbers.setText(self.numb)

    def satu_per_x(self):
        try:
            self.algo = "1/" + str(self.numb)
            self.algorithms.setText(f"1/({self.numb})")
            self.numb = str(eval(self.algo))
            self.numbers.setText(self.numb)
        except ZeroDivisionError:
            self.numbers.setText("Cant divide with a Zero")
        self.algo = self.numb
        self.numb = ""

    def squared(self):
        squared_value = float(self.numb) ** 2
        squared_value = str(squared_value)
        self.algorithms.setText(f"sqr({self.numb})")
        self.numbers.setText(squared_value)
        self.numb = squared_value

    def square_root(self):
        root_value = math.sqrt(int(self.numb))
        root_value = str(root_value)
        self.algorithms.setText(f"√({self.numb})")
        self.numbers.setText(root_value)
        self.numb = root_value


    def percentage(self):
        if self.algo == "":
            self.numb = "0"
            self.numbers.setText(self.numb)
        else:
            whole = int(self.algo[:-1])
            percentage = int(self.numb)
            percentage_result = float((percentage * whole) / 100)
            percentage_result = str(percentage_result)
            self.algorithms.setText(self.algo)
            self.numbers.setText(percentage_result)
            self.numb = percentage_result

    def dot(self, dots):
        if "." not in self.numb:
            self.numb += dots
            self.numbers.setText(self.numb)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_0:
            self.angka("0")
        elif e.key() == Qt.Key_1:
            self.angka("1")
        elif e.key() == Qt.Key_2:
            self.angka("2")
        elif e.key() == Qt.Key_3:
            self.angka("3")
        elif e.key() == Qt.Key_4:
            self.angka("4")
        elif e.key() == Qt.Key_5:
            self.angka("6")
        elif e.key() == Qt.Key_6:
            self.angka("6")
        elif e.key() == Qt.Key_7:
            self.angka("7")
        elif e.key() == Qt.Key_8:
            self.angka("8")
        elif e.key() == Qt.Key_9:
            self.angka("9")
        elif e.key() == Qt.Key_Period:
            self.dot(".")
        elif e.key() == Qt.Key_Slash:
            self.click_operator("/")
        elif e.key() == Qt.Key_Asterisk:
            self.click_operator("*")
        elif e.key() == Qt.Key_Minus:
            self.click_operator("-")
        elif e.key() == Qt.Key_Plus:
            self.click_operator("+")
        elif e.key() == Qt.Key_Equal or Qt.Key_Return:
            self.tombol_hasil()
        elif e.key() == Qt.Key_Delete:
            self.ce_button()
        elif e.key() == Qt.Key_Escape:
            self.c_button()
        elif e.key() == Qt.Key_Backspace:
            self.backspace_button()
        elif e.key() == Qt.Key_Q:
            self.squared()
        elif e.key() == Qt.Key_At:
            self.square_root()
        elif e.key() == Qt.Key_Percent:
            self.percentage()
        elif e.key() == Qt.Key_R:
            self.satu_per_x()

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()