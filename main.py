import sys, math
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.Qt import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(292, 223, 400, 635)
        self.setWindowIcon(QIcon('calculator icon.png'))

        self.numb, self.algo = "0", ""

        self.algorithms, self.numbers = QLabel(self), QLabel(self)

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

        self.division = QPushButton("÷", self)
        self.times = QPushButton("×", self)
        self.minus = QPushButton("-", self)
        self.plus = QPushButton("+", self)

        self.equals = QPushButton("=", self)
        self.ce = QPushButton("CE", self)
        self.c = QPushButton("C", self)
        self.backspace = QPushButton("⌫", self)

        self.square = QPushButton("x²", self)
        self.square_root = QPushButton("²√x", self)
        self.coma = QPushButton(".", self)
        self.percent = QPushButton("%", self)
        self.reciprocal = QPushButton("⅟x", self)
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
        grid.addWidget(self.coma, 7, 2)
        grid.addWidget(self.equals, 7, 3)

        grid.addWidget(self.button_1, 6, 0)
        grid.addWidget(self.button_2, 6, 1)
        grid.addWidget(self.button_3, 6, 2)
        grid.addWidget(self.plus, 6, 3)

        grid.addWidget(self.button_4, 5, 0)
        grid.addWidget(self.button_5, 5, 1)
        grid.addWidget(self.button_6, 5, 2)
        grid.addWidget(self.minus, 5, 3)

        grid.addWidget(self.button_7, 4, 0)
        grid.addWidget(self.button_8, 4, 1)
        grid.addWidget(self.button_9, 4, 2)
        grid.addWidget(self.times, 4, 3)

        grid.addWidget(self.reciprocal, 3, 0)
        grid.addWidget(self.square, 3, 1)
        grid.addWidget(self.square_root, 3, 2)
        grid.addWidget(self.division, 3, 3)

        grid.addWidget(self.percent, 2, 0)
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
        self.coma.setObjectName("numbers")
        self.plus_minus.setObjectName("numbers")

        self.ce.setObjectName("other_function")
        self.c.setObjectName("other_function")
        self.backspace.setObjectName("operators")
        self.division.setObjectName("operators")
        self.times.setObjectName("operators")
        self.minus.setObjectName("operators")
        self.plus.setObjectName("operators")
        self.square.setObjectName("other_function")
        self.square_root.setObjectName("other_function")
        self.percent.setObjectName("other_function")
        self.reciprocal.setObjectName("other_function")

        self.equals.setObjectName("equals")

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
            QPushButton#other_function{
                font-size:16px;
                padding:23px;
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#other_function:hover{
                background-color:#3b3b3b;
                color:#ffffff;
            }
            QPushButton#other_function:pressed{
                background-color:#323232;
                color:#ffffff;
            }
            QPushButton#equals{
                font-size:27px;
                padding:15px;
                background-color:#76b9ed;
            }
            QPushButton#equals:hover{
                background-color:#6da9d8;
            }
            QPushButton#equals:pressed{
                background-color:#649ac3;
            }


        """)

        self.button_0.clicked.connect(lambda: self.number("0"))
        self.button_1.clicked.connect(lambda: self.number("1"))
        self.button_2.clicked.connect(lambda: self.number("2"))
        self.button_3.clicked.connect(lambda: self.number("3"))
        self.button_4.clicked.connect(lambda: self.number("4"))
        self.button_5.clicked.connect(lambda: self.number("5"))
        self.button_6.clicked.connect(lambda: self.number("6"))
        self.button_7.clicked.connect(lambda: self.number("7"))
        self.button_8.clicked.connect(lambda: self.number("8"))
        self.button_9.clicked.connect(lambda: self.number("9"))
        self.coma.clicked.connect(lambda: self.dot())

        self.division.clicked.connect(lambda: self.click_operator("/"))
        self.times.clicked.connect(lambda: self.click_operator("*"))
        self.minus.clicked.connect(lambda: self.click_operator("-"))
        self.plus.clicked.connect(lambda: self.click_operator("+"))

        self.equals.clicked.connect(self.equals_button)
        self.c.clicked.connect(self.c_button)
        self.ce.clicked.connect(self.ce_button)
        self.backspace.clicked.connect(self.backspace_button)
        self.plus_minus.clicked.connect(self.minus_plus)
        self.reciprocal.clicked.connect(self.reciprocal_function)
        self.square.clicked.connect(self.squared)
        self.square_root.clicked.connect(self.squared_root)
        self.percent.clicked.connect(self.percentage)

    def number(self, num):
        if len(self.numb) < 16:
            if self.numb == "0":
                self.numb = num
            else:
                self.numb += num
        self.numbers.setText(format_number_commas(format_display_number(self.numb)))

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

            self.algorithms.setText(formatted_display_algorithms(self.algo))
            self.numb = "0"
            self.numbers.setText(format_display_number(self.numb))
        except ZeroDivisionError:
            self.numb = "0"
            self.algo = ""
            self.numbers.setText("Cant divide by Zero")
            self.algorithms.setText(formatted_display_algorithms(self.algo))

    def equals_button(self):
        try:
            if not self.algo:
                return
            if self.algo[-1] in "+-*/":
                self.algo = self.algo + self.numb
                result = eval(self.algo)
                if result.is_integer():
                    result = int(result)
                self.algorithms.setText(formatted_display_algorithms(self.algo) + " =")
                self.numbers.setText(format_number_commas(format_display_number(str(result))))
                self.algo = str(result)
                self.numb = ""
            elif self.algo[-1] not in "+-*/":
                pass
            else:
                self.algo = self.numb

        except ZeroDivisionError:
            self.numb = "0"
            self.algo = ""
            self.numbers.setText("Cant divide by Zero")
            self.algorithms.setText(self.algo)

    def c_button(self):
        self.algo = ""
        self.numb = "0"
        self.numbers.setText(format_display_number(self.numb))
        self.algorithms.setText("")

    def ce_button(self):
        self.numb = "0"
        self.numbers.setText(format_display_number(self.numb))

    def backspace_button(self):
        self.numb = self.numb[:-1]
        if self.numb:
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))
        else:
            self.numb = "0"
            self.numbers.setText(format_display_number(self.numb))

    def minus_plus(self):
        if self.numb == "0":
            pass
        elif self.numb[0] == "-":
            self.numb = self.numb[1:]
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))
        else:
            self.numb = "-" + self.numb
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))

    def reciprocal_function(self):
        try:
            self.algo = "1/" + str(self.numb)
            self.algorithms.setText(formatted_display_algorithms(f"1/({self.numb})"))
            self.numb = str(eval(self.algo))
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))
        except ZeroDivisionError:
            self.numbers.setText("Cant divide with a Zero")
        self.algo = self.numb
        self.numb = ""

    def squared(self):
        squared_value = float(self.numb) ** 2
        self.algorithms.setText(formatted_display_algorithms(f"sqr({self.numb})"))
        if squared_value.is_integer():
            self.numbers.setText(str(int(squared_value)))
        else:
            self.numbers.setText(str(squared_value))
        self.numb = squared_value

    def squared_root(self):
        root_value = math.sqrt(int(self.numb))
        self.algorithms.setText(formatted_display_algorithms(f"√({self.numb})"))
        if root_value.is_integer():
            self.numbers.setText(str(int(root_value)))
        else:
            self.numbers.setText(str(root_value))
        self.numb = root_value

    def percentage(self):
        if self.algo == "":
            self.numb = "0"
            self.numbers.setText(self.numb)
        else:
            percentage = float(self.algo[:-1]) * (int(self.numb) / 100)
            if percentage.is_integer():
                percentage = int(percentage)
            self.algorithms.setText(formatted_display_algorithms(self.algo))
            self.numb = str(percentage)
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))

    def dot(self):
        if "." not in self.numb:
            self.numb += "."
            self.numbers.setText(format_number_commas(format_display_number(self.numb)))

    def keyPressEvent(self, e):
        match e.key():
            case Qt.Key_0:
                self.number("0")
            case Qt.Key_1:
                self.number("1")
            case Qt.Key_2:
                self.number("2")
            case Qt.Key_3:
                self.number("3")
            case Qt.Key_4:
                self.number("4")
            case Qt.Key_5:
                self.number("5")
            case Qt.Key_6:
                self.number("6")
            case Qt.Key_7:
                self.number("7")
            case Qt.Key_8:
                self.number("8")
            case Qt.Key_9:
                self.number("9")
            case Qt.Key_Period:
                self.dot()
            case Qt.Key_Slash:
                self.click_operator("/")
            case Qt.Key_Asterisk:
                self.click_operator("*")
            case Qt.Key_Minus:
                self.click_operator("-")
            case Qt.Key_Plus:
                self.click_operator("+")
            case Qt.Key_Equal:
                self.equals_button()
            case Qt.Key_Delete:
                self.ce_button()
            case Qt.Key_Escape:
                self.c_button()
            case Qt.Key_Backspace:
                self.backspace_button()
            case Qt.Key_Q:
                self.squared()
            case Qt.Key_At:
                self.squared_root()
            case Qt.Key_Percent:
                self.percentage()
            case Qt.Key_R:
                self.reciprocal_function()

def formatted_display_algorithms(algorithms):
    return algorithms.replace("*", "×").replace("/", "÷").replace("-", "-").replace("+", "+")

def format_display_number(number):
    if number.endswith(".") or "." in number:
        display_number = number
    else:
        try:
            display_number = str(int(float(number)))
        except ValueError:
            display_number = number

    return display_number

def format_number_commas(number):
    is_negative = number.startswith('-')
    if is_negative:
        number = number[1:]

    parts = number.split('.')
    integer_part = parts[0]

    formatted_integer = ""
    for i in range(len(integer_part) - 1, -1, -1):
        formatted_integer = integer_part[i] + formatted_integer
        if (len(integer_part) - i) % 3 == 0 and i > 0:
            formatted_integer = "," + formatted_integer

    if len(parts) > 1:
        formatted_number = formatted_integer + "." + parts[1]
    else:
        formatted_number = formatted_integer

    if is_negative:
        formatted_number = "-" + formatted_number

    return formatted_number

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
