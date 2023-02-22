import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy

class Calculadora(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora Python')
        self.setFixedSize(500,500)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.display.setStyleSheet(
            '* {background: #EEE; color: #000; font-size: 30px;}'
        )

        self.add_btn(QPushButton('7'), 1, 0, 1, 1) # forma de adicionar os botões na tela, tem que se atentar para as rows e cols do grid
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton(' * '), 1, 3, 1, 1)
        self.add_btn(QPushButton('C'), 1, 4, 1, 1, self.clear,'background: #d5580d; color: #eee ; font-weight: 700; ; font-size: 20px; border-radius: 10px;') 

        # função para não deixar os botões de clear escreverem na tela = lambda: self.display.setText(''),

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton(' - '), 2, 3, 1, 1)
        self.add_btn(QPushButton('del'), 2, 4, 1, 1, lambda: self.display.setText(self.display.text() [:-1] ),'background: #13823a; color: #eee ; font-weight: 700; font-size: 20px; border-radius: 10px;')
        
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton(' + '), 3, 3, 1, 1)
        self.add_btn(QPushButton(' = '), 3, 4, 1, 1, self.eval_igual,'background: #095177; color: #eee ; font-weight: 700; font-size: 20px; border-radius: 10px;')

        self.add_btn(QPushButton('0'), 4, 1, 1, 1)
        self.add_btn(QPushButton(' ^ '), 4, 2, 1, 1, lambda: self.display.setText(self.display.text() + ' ** '))
        self.add_btn(QPushButton(' / '), 4, 3, 1, 1)
        self.add_btn(QPushButton('.'), 4, 0, 1, 1)
        self.add_btn(QPushButton('SAIR'), 4, 4, 1, 1, lambda: exit())

        

        self.setCentralWidget(self.cw)

    def add_btn(self,btn,row,col,rowspan,colspan, funcao=None, style=None): # método para adicionar os botões na tela 

        self.grid.addWidget(btn,row,col,rowspan,colspan)
        
        if not funcao:
            btn.clicked.connect( # setar uma 'conexão' entre o botão e display para mostrar o texto na tela  

                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
            
        else:
            btn.clicked.connect(funcao)

        if style: # valida se tem algum estilo nos btns, se houver, vai aplicar.
            btn.setStyleSheet(style)
        else:
            btn.setStyleSheet(open('PyQT5\calc.css').read())

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )

        except Exception:
            self.display.setText("Conta Inválida !")

    def clear(self):
        self.display.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
