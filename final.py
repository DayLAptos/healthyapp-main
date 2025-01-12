from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from instr import *


from instr import *
from second import *
     
class FinalWin(QWidget):
    def __init__(self, exp):
       super().__init__()
       self.exp
       self.initUI()
       self.connects()
       self.set_appear()
       self.show()
    def initUI(self):

       self.hello_text = QLabel(txt_hello)

       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)    
       self.setLayout(self.layout_line)
    def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(weight, height)
       self.move(win_x, win_y)
    def results(self):
        if self.exp.age < 7:
            self.index = 0
            return 'нет данных для такого возраста'
        self.index = (4*(int(self.exp.t1)+ int(self.exp.t2)+int(self.exxp.t3))-200)/10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.4 and self.index >= 10:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age >= 15 or self.exp.age <= 18:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
app = QApplication([])
mw = MainWin()
app.exec_()
