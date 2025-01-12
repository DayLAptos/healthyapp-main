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
        self.index = (4*(int(self.exp.t1)+ int(self.exp.t2)+int(self.exxp.t3))-200)/10

app = QApplication([])
mw = MainWin()
app.exec_()
