from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtCore import QTime, QTimer
from instr import *

from second import *
     
class MainWin(QWidget):
   def __init__(self):
       super().__init__()
       self.initUI()
       self.connects()
       self.set_appear()
       self.show()
   def initUI(self):
       self.btn_next = QPushButton(txt_next, self)
       self.hello_text = QLabel(txt_hello)
       self.instruction = QLabel(txt_instruction)
       self.layout_line = QVBoxLayout()
       self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
       self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)         
       self.setLayout(self.layout_line)
   def next_click(self):
       self.w = TestWin()
       self.hide()
   def connects(self):
       self.btn_next.clicked.connect(self.next_click)
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(weight, height)
       self.move(win_x, win_y)



app = QApplication([])
mw = MainWin()
app.exec_()

