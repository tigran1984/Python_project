#!/usr/bin/python
                    

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Dialog_window(QDialog):

        def __init__(self, parent = None):
                QDialog.__init__(self, parent)
                self.initUI()

        def initUI(self):
                                                                                
                
                self.lbl1 = QLabel("Name")
                self.nm = QLineEdit()
                self.lbl2 = QLabel("Address")
                self.add1 = QLineEdit()
                self.add2 = QLineEdit()
                self.fbox = QFormLayout()
                self.fbox.addRow(self.lbl1,self.nm )

                self.vbox = QVBoxLayout()
                self.vbox.addWidget(self.add1)
                self.vbox.addWidget(self.add2)
                self.fbox.addRow(self.lbl2, self.vbox)
                self.hbox = QHBoxLayout()

                self.r1 = QRadioButton("Red")
                self.r2 = QRadioButton("Green")
                self.r3 = QRadioButton("Blue")
                self.hbox.addWidget(self.r1)
                self.hbox.addWidget(self.r2)
                self.hbox.addWidget(self.r3)
                self.fbox.addRow(QPushButton("OK"),QPushButton("Cancel"))
                self.fbox.addRow(QLabel("color"),self.hbox)

                self.setLayout(self.fbox)

                self.setWindowTitle("PyQt")
                self.show()


class Main_Window( QMainWindow):
    def __init__(self, parent = None):
        super(Main_Window,self).__init__(parent)
        self.initUI()

    def initUI(self):
        dialog_window = QAction(QIcon('plugin0.png'), '&DIALOG WINDOW', self)
#        dialog_window =
#        dialog_window =
        dialog_window.triggered.connect(self.showdialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(dialog_window)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')    
        self.show()

    def showdialog(self):
        d = Dialog_window()
        d.exec_()

        
def main():
    
    app = QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

