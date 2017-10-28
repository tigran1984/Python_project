#!/usr/bin/python

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import time

class ProgBar(QDialog):
    
    def __init__(self,min_value,max_value):
        super(ProgBar, self).__init__()
        self.min_value = min_value
        self.max_value = max_value
        self.step = min_value
        self.initUI()

        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setMinimum(self.min_value) 
        self.pbar.setMaximum(self.max_value)


        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        self.pbar.setValue(self.step)

    def doStep(self):
        self.step = self.step + 1  
        self.pbar.setValue(self.step)

def main():
    
    app = QApplication(sys.argv)
    ex = ProgBar(1,5)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
