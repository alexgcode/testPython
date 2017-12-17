import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton #variables globales
from PyQt5.QtGui import QIcon

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		btn = QPushButton('Button', self)
		btn.resize(btn.sizeHint())
		btn.move(50,50)

		self.setGeometry(300,300,300,220)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('icon.png')) 
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()	#instanciacion de la clase(creacion de objeto) para que se muestre la ventana
	print(ex)
	sys.exit(app.exec_())