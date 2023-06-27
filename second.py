from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QLineEdit
from settings import *
from PyQt5.QtGui import * 
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
		self.timer = QLabel('00:00:15')
		self.timer.setFont(QFont('Arial', 25))
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
		self.V_LineRight.addWidget(self.timer,alignment = Qt.AlignCenter)

		self.H_Line = QHBoxLayout()
		self.H_Line.addLayout(self.V_LineLeft)
		self.H_Line.addLayout(self.V_LineRight)
		self.setLayout(self.H_Line)


	def connects(self):
		pass
	# 	self.button.clicked.connect(self.next_click)

	# def next_click(self):
	# 	self.hide()