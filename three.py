from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from settings import *
from second import *
class Experiment():
	def __init__(self,age,p1,p2,p3):
		self.age = age
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3



class FinalWin(QWidget):
	def __init__(self,exp):
		super().__init__()
		self.set_appear()
		self.exp = exp 
		self.index=(4*(int(self.exp.p1)+int(self.exp.p2)+int(self.exp.p3))-200)/10
		self.initUI()
		self.show()



	def set_appear(self):
		self.resize(w_width,w_height)
		self.setWindowTitle('Резултьаты')

	def initUI(self):
		self.indexR = QLabel("Индекс Руфье:" + str(self.index))
		self.indexR.setFont(QFont('Arial', 20))
		self.serdse = QLabel("Работоспособность сердца:" )
		self.serdse.setFont(QFont('Arial', 20))

		self.V_Line = QVBoxLayout()
		self.V_Line.addWidget(self.indexR,alignment = Qt.AlignCenter)
		self.V_Line.addWidget(self.serdse,alignment = Qt.AlignCenter)
		self.setLayout(self.V_Line)

	#  def results(self):
 #       if self.exp.age < 7:
 #           self.index = 0
 #           return "нет данных для такого возраста"
 #       self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
 #       if self.exp.age == 7 or self.exp.age == 8:
 #           if self.index >= 21:
 #               return txt_res1
 #           elif self.index < 21 and self.index >= 17:
 #               return txt_res2
 #           elif self.index < 17 and self.index >= 12:
 #               return txt_res3
 #           elif self.index < 12 and self.index >= 6.5:
 #               return txt_res4
 #           else:
 #               return txt_res5
 #       if self.exp.age == 9 or self.exp.age == 10:
 #           if self.index >= 19.5:
 #               return txt_res1
 #           elif self.index < 19.5 and self.index >= 15.5:
 #               return txt_res2
 #           elif self.index < 15.5 and self.index >= 10.5:
 #               return txt_res3
 #           elif self.index < 10.5 and self.index >= 5:
 #               return txt_res4
 #           else:
 #               return txt_res5
 #       if self.exp.age == 11 or self.exp.age == 12:
 #           if self.index >= 18:
 #               return txt_res1
 #           elif self.index < 18 and self.index >= 14:
 #               return txt_res2
 #           elif self.index < 14 and self.index >= 9:
 #               return txt_res3
 #           elif self.index < 9 and self.index >= 3.5:
 #               return txt_res4
 #           else:
 #               return txt_res5
 #       if self.exp.age == 13 or self.exp.age == 14:
 #           if self.index >= 16.5:
 #               return txt_res1
 #           elif self.index < 16.5 and self.index >= 12.5:
 #               return txt_res2
 #           elif self.index < 12.5 and self.index >= 7.5:
 #               return txt_res3
 #           elif self.index < 7.5 and self.index >= 2:
 #               return txt_res4
 #           else:
 #               return txt_res5
 #       if self.exp.age >= 15:
 #           if self.index >= 15:
 #               return txt_res1
 #           elif self.index < 15 and self.index >= 11:
 #               return txt_res2
 #           elif self.index < 11 and self.index >= 6:
 #               return txt_res3
 #           elif self.index < 6 and self.index >= 0.5:
 #               return txt_res4
 #           else:
 #               return txt_res5

	# 