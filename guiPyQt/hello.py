import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton #variables globales
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		

		self.setGeometry(300,300,300,220)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('icon.png')) 
		self.home()

	def home(self):
		btn = QPushButton('Quit', self)
		btn.clicked.connect(self.quitmethod)	#cerrar programa
		btn.resize(btn.sizeHint())
		btn.move(50,50)
		self.show()

	def quitmethod():
		QCoreApplication.instance().quit

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()	#instanciacion de la clase(creacion de objeto) para que se muestre la ventana
	sys.exit(app.exec_())