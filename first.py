from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from settings import *
from second import *
class MainWin(QWidget):
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
		self.title = QLabel(txt_hello)
		self.title2 = QLabel(txt_instruction)
		self.button = QPushButton('Начать')

		self.main_line = QVBoxLayout()
		self.main_line.addWidget(self.title,alignment= Qt.AlignCenter)
		self.main_line.addWidget(self.title2,alignment= Qt.AlignCenter)
		self.main_line.addWidget(self.button,alignment= Qt.AlignCenter)
		self.setLayout(self.main_line)


	def connects(self):
		self.button.clicked.connect(self.next_click)

	def next_click(self):
		self.hide()
		self.second = TestWin()





app = QApplication([])
WinWin = MainWin()
app.exec_()
