import sys
from PyQt5 import QtWidgets, uic

'''
jamersonwalderson@gmail.com

Lista simples em python usando PyQt5

materiais de apoio
    doc - https://www.riverbankcomputing.com/static/Docs/PyQt4/qlistwidget.html
    canal Coding Bunny - https://www.youtube.com/watch?v=c2d3AvC9xZE
'''

janela = QtWidgets.QApplication(sys.argv)
interface = uic.loadUi('listaGui.ui')

def ADD():
    interface.list.addItem(interface.txtAdd.text())
def CLEAR():
    interface.list.clear()
def DEL():
    interface.list.takeItem(interface.list.currentRow())


interface.btAdd.clicked.connect(ADD)
interface.btClear.clicked.connect(CLEAR)
interface.btDelete.clicked.connect(DEL)

interface.show()
sys.exit(janela.exec())