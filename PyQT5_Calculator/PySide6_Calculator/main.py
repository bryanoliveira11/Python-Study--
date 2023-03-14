import sys
from PySide6.QtWidgets import QApplication,QLabel
from PySide6.QtGui import QIcon
from main_window import MainWindow
from info import Info
from display import Display
from buttons import ButtonsGrid
from styles import setupTheme
from variables import WINDOW_ICON_PATH

def temp_label(texto):
    label1 = QLabel(texto)
    label1.setStyleSheet('font-size:150px;')
    return label1

if __name__ == '__main__':
    # cria aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # info

    info = Info('Sua Conta')
    window.addWidgetToVLayout(info)

    # define o icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    # display
    display = Display('')
    window.addWidgetToVLayout(display)

    # grid
    buttonsgrid = ButtonsGrid(display,info,window)
    window.vLayout.addLayout(buttonsgrid)


    # executa tudo
    window.show()
    window.adjustFixedSize()
    app.exec()