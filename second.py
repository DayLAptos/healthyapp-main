from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel, QWidget, QApplication
from PyQt5.QtCore import QTime, QTimer
import time
from instr import *
from my_app import *
app = QApplication([])
class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3
class TestWin(QWidget):
    def __init__(self):
       super().__init__()
       self.initUI()
       self.connects()
       self.set_appear()
       self.show()

    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_sits(self):
        global time
        time = QTime(0,0,30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer_test(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_x, win_y)
        self.resize(weight,height)
    def initUI(self):
        self.btn_test1 = QPushButton(txt_next, self)
        self.btn_test2 = QPushButton(txt_next, self)
        self.btn_test3 = QPushButton(txt_next, self)
        self.btn_next = QPushButton(txt_next, self)
        self.name_text = QLabel('Ваше ФИО')
        self.age_text = QLabel('Ваш возраст')
        self.test1_text = QLabel(txt_test1)
        self.test2_text = QLabel(txt_test2)
        self.test3_text = QLabel(txt_test3)
        self.timer = QLabel(self.time)
        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hintage)
        self.line_test2 = QLineEdit(txt_hintage)
        self.line_test3 = QLineEdit(txt_hintage)
        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.name_text, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.age_text, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.test1_text, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.test2_text, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.test3_text, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.timer, alignment = Qt.AlignLeft)
        self.r_line.addWidget(self.btn_next, alignment = Qt.AlignLeft)
        self.h_line.addLayout(self.r_line)  
        self.h_line.addLayout(self.l_line)
        self.setLayout(self.h_line)
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(), self.line_test1.text, self.line_test2.text, self.line_test3.text)
        self.fw = FinalWin(self.exp)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer1Event)
        self.btn_test2.clicked.connect(self.timer2Event)
        self.btn_test3.clicked.connect(self.timer3Event)

mw = TestWin()

mw.show()
app.exec_()