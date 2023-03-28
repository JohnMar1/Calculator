from typing import Container
import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulačka")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []

        self.show()
    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout()) 

        #tlačítka
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton("Enter", clicked = self.func_result)
        btn_clear = qtw.QPushButton("Vymazat", clicked = self.clear_calc)
        btn1 = qtw.QPushButton("1", clicked = lambda:self.num_press("1"))
        btn2 = qtw.QPushButton("2", clicked = lambda:self.num_press("2"))
        btn3 = qtw.QPushButton("3", clicked = lambda:self.num_press("3"))
        btn4 = qtw.QPushButton("4", clicked = lambda:self.num_press("4"))
        btn5 = qtw.QPushButton("5", clicked = lambda:self.num_press("5"))
        btn6 = qtw.QPushButton("6", clicked = lambda:self.num_press("6"))
        btn7 = qtw.QPushButton("7", clicked = lambda:self.num_press("7"))
        btn8 = qtw.QPushButton("8", clicked = lambda:self.num_press("8"))
        btn9 = qtw.QPushButton("9", clicked = lambda:self.num_press("9"))
        btn0 = qtw.QPushButton("0", clicked = lambda:self.num_press("0"))
        btn_plus = qtw.QPushButton("+", clicked = lambda:self.func_press("+"))
        btn_minus = qtw.QPushButton("-", clicked = lambda:self.func_press("-"))
        btn_multiply = qtw.QPushButton("*", clicked = lambda:self.func_press("*"))
        btn_divide = qtw.QPushButton("÷", clicked = lambda:self.func_press("/"))

        #pozice tlačítek
        container.layout().addWidget(self.result_field,0,0,1,4)
        container.layout().addWidget(btn_result,1,0,1,2)
        container.layout().addWidget(btn_clear,1,2,1,2)
        container.layout().addWidget(btn1,2,0,1,1)
        container.layout().addWidget(btn2,2,1,1,1)
        container.layout().addWidget(btn3,2,2,1,1)
        container.layout().addWidget(btn4,3,0,1,1)
        container.layout().addWidget(btn5,3,1,1,1)
        container.layout().addWidget(btn6,3,2,1,1)
        container.layout().addWidget(btn7,4,0,1,1)
        container.layout().addWidget(btn8,4,1,1,1)
        container.layout().addWidget(btn9,4,2,1,1)
        container.layout().addWidget(btn0,5,0,1,3)
        container.layout().addWidget(btn_plus,2,3,1,1)
        container.layout().addWidget(btn_minus,3,3,1,1)
        container.layout().addWidget(btn_multiply,4,3,1,1)
        container.layout().addWidget(btn_divide,5,3,1,1)
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText("".join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)
    def func_press(self, operator):
        temp_string = "".join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText("".join(self.fin_nums))
    def func_result(self):
        fin_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        if fin_string != "":
            ends_with_sign = fin_string[-1]
        else: ends_with_sign = "nic"
        if ends_with_sign == "+" or ends_with_sign == "-" or ends_with_sign == "*" or ends_with_sign == "/":
            self.result_field.setText("Nepoužívejte znaménka na konci příkladu! Zmáčkni tlačítko Vymazat.")
        elif fin_string == "":
            self.result_field.setText("Prosím zmáčkni Vymazat a zadej příklad.") 
        else:
            result_string = eval(fin_string)
            fin_string += "="
            fin_string = str(result_string)
            self.result_field.setText(fin_string)
    def clear_calc(self):
        self.result_field.clear()
        self.fin_nums = []
        self.temp_nums = []

app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create("Fusion"))
app.exec_()
#made by JohnMar1 (Jan Marval)
