from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QLineEdit
from settings import *
from PyQt5.QtGui import *
from three import* 
class TestWin(QWidget):
	def __init__(self):
		super().__init__()
		self.set_appear()
		self.initUI()
		self.connects()
		self.show()
		
	def set_appear(self):
		self.resize(w_width,w_height)
		self.setWindowTitle('Здорово')

	def initUI(self):
		self.text1 = QLabel(txt_title)
		self.text2 = QLabel(txt_name)
		self.text3 = QLabel(txt_test1)
		self.text4 = QLabel(txt_test2)
		self.text5 = QLabel(txt_test3)
		self.timeremertext = QLabel('00:00:15')
		self.timeremertext.setFont(QFont('Arial', 25))
		self.text6 = QLabel('Полных лет:')

		self.button1 = QPushButton(txt_starttest1)
		self.button2 = QPushButton(txt_starttest2)
		self.button3 = QPushButton(txt_starttest3)
		self.button4 = QPushButton(txt_sendresults)


		self.okno1 = QLineEdit(txt_hintname)
		self.okno2 = QLineEdit(txt_hintage)
		self.okno3 = QLineEdit(txt_hintage)
		self.okno4 = QLineEdit(txt_hintage)
		self.okno5 = QLineEdit(txt_hintage)

		self.V_LineLeft = QVBoxLayout()
		self.V_LineLeft.addWidget(self.text2,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.okno1,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.text6,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.okno2,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.text3,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.button1,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.okno3,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.text4,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.button2,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.text5,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.button3,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.okno4,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.okno5,alignment = Qt.AlignCenter)
		self.V_LineLeft.addWidget(self.button4,alignment = Qt.AlignCenter)

		self.V_LineRight = QVBoxLayout()
		self.V_LineRight.addWidget(self.timeremertext,alignment = Qt.AlignCenter)

		self.H_Line = QHBoxLayout()
		self.H_Line.addLayout(self.V_LineLeft)
		self.H_Line.addLayout(self.V_LineRight)
		self.setLayout(self.H_Line)


	def connects(self):
		self.button4.clicked.connect(self.next_click)
		self.button1.clicked.connect(self.timer1)
		self.button2.clicked.connect(self.timer2)
		self.button3.clicked.connect(self.timer3)

	def next_click(self):
		self.hide()
		self.exp = Experiment(self.okno2.text(), self.okno3.text(), self.okno4.text(), self.okno5.text())
		self.three = FinalWin(self.exp)
	
	def timer1(self):
		global time
		time = QTime(0,0,15)
		self.timer = QTimer()
		self.timer.timeout.connect(self.timer1Event)
		self.timer.start(1000)

	def timer1Event(self):
		global time
		time = time.addSecs(-1)
		self.timeremertext.setText(time.toString("hh:mm:ss"))

		if time.toString("hh:mm:ss") == "00:00:00":
			self.timer.stop()

	def timer2(self):
		global time
		time = QTime(0,0,30)
		self.timer = QTimer()
		self.timer.timeout.connect(self.timer2Event)
		self.timer.start(1500)



	def timer2Event(self):
		global time
		time = time.addSecs(-1)
		self.timeremertext.setText(time.toString("hh:mm:ss"))

		if time.toString("hh:mm:ss") == "00:00:00":
			self.timer.stop()


	def timer3(self):
		global time
		time = QTime(0,1,0)
		self.timer = QTimer()
		self.timer.timeout.connect(self.timer3Event)
		self.timer.start(1500)




	def timer3Event(self):
		global time

		

		time = time.addSecs(-1)
		
		self.timeremertext.setText(time.toString("hh:mm:ss"))
		if time.toString("hh:mm:ss") == "00:00:59":
			self.timeremertext.setStyleSheet("color:rgb(0,255,0)")

		if time.toString("hh:mm:ss") == "00:00:45":
			self.timeremertext.setStyleSheet("color:rgb(0,0,0)")
		if time.toString("hh:mm:ss") == "00:00:15":
			self.timeremertext.setStyleSheet("color:rgb(0,255,0)")


		if time.toString("hh:mm:ss") == "00:00:00":
			self.timer.stop()
		
