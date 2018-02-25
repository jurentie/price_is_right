import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = '$$$ The Price is Right $$$'
        self.left = 1100
        self.top = 350
        self.width = 500
        self.height = 600
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(254,189,105))
        self.setPalette(p)

        self.gameCode = QLabel('',self)
        self.gameCode.setGeometry(10,10,400,50)
        self.p1Output = QLabel('', self)
        self.p1Output.setGeometry(10,10,400,50)

        self.productName = QLabel('',self)
        self.productName.setGeometry(10,10,400,50)

        self.enterGuess = QLabel('', self)
        self.enterGuess.setGeometry(10,10,400,50)

        self.startGameButton = QPushButton('Start A Game', self)
        self.startGameButton.setToolTip('startGame')
        self.startGameButton.move(150,200) 
        self.startGameButton.resize(200, 50)
        self.startGameButton.clicked.connect(self.start_game)

        self.joinGameButton = QPushButton('Join A Game', self)
        self.joinGameButton.setToolTip('joinGame')
        self.joinGameButton.move(150,275) 
        self.joinGameButton.resize(200,50)
        self.joinGameButton.clicked.connect(self.join_game)

        self.submitButton = QPushButton('Submit', self)
        self.submitButton.setToolTip('joinGame')
        self.submitButton.move(150,410) 
        self.submitButton.resize(0,0)
        self.submitButton.clicked.connect(self.submit_button)

        self.image = QLabel(self)
        self.pixmap = QPixmap('./fart_ring.jpg')
        self.pixmap = self.pixmap.scaled(200,200)

        self.textbox = QLineEdit(self)
        self.textbox.move(150, 200)
        self.textbox.resize(0,0) 

        self.show()

    @pyqtSlot()
    def start_game(self):
        newfont = QFont("Times", 16, QFont.Bold)
        self.gameCode.setText('X45HLK')
        self.gameCode.setFont(newfont)
        self.gameCode.move(200, 250)
        self.startGameButton.resize(0,0)
        self.joinGameButton.resize(0,0)

    @pyqtSlot()
    def join_game(self):
        self.startGameButton.resize(0,0)
        self.joinGameButton.clicked.connect(self.join_game_code)
        self.textbox.resize(200,25)

    @pyqtSlot()
    def join_game_code(self):
        print("Joining Game")
        self.image.setPixmap(self.pixmap)
        self.image.resize(200,200)
        self.image.move(150,100)
        self.textbox.resize(0,0)
        self.joinGameButton.resize(0,0)
        self.productName.setText('The Moon Ring')
        self.productName.move(200,300)
        self.enterGuess.setText('Enter Your Guess: ')
        self.enterGuess.move(120,350)
        self.textbox.resize(100,25)
        self.textbox.move(280, 365)
        self.submitButton.resize(200,50)
        pass

    @pyqtSlot()
    def submit_button(self):
        print('submitted')
        pass
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())