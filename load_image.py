#!/usr/bin/python

#import sys
#from PyQt4 import QtGui
#app = QtGui.QApplication(sys.argv)
#window = QtGui.QMainWindow()
#window.setGeometry(0, 0, 400, 400)
#pic = QtGui.QLabel(window)
#pic.setGeometry(10, 10, 400, 400)
#pixmap = QtGui.QPixmap('myimage.gif')
#pixmap = pixmap.scaledToWidth(500)
#pic.setPixmap(pixmap)
#
#window.show()
#sys.exit(app.exec_())
#effect	= QGraphicsBlurEffect() 
#x:effect.setBlurRadius(10)	  
#label.setGraphicsEffect(effect)  


from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys


class main_window(QWidget):
    def __init__(self):
        super(main_window, self).__init__()
        self.init_ui()

    def init_ui(self):  
        self.setWindowTitle("Blur Effect")
        self.box = QBoxLayout(QBoxLayout.TopToBottom, self);
        self.setLayout(self.box)
        self.button = QPushButton("Blur");
        self.label = QLabel()    
        self.box.addWidget(self.button)
        self.box.addWidget(self.label)
        self.image = QImage('myimage.gif')
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.button.pressed.connect(self.blur_picture)

    def blur_picture(self):
        h = self.image.height()
        w = self.image.width()
        for x in range(0, 100):
          for y in range(0, 100):
                self.image.setPixel(x, y, self.image.pixel(x + 100, y + 100))
        self.repaint(self.rect())
        
        #self.label.setPixmap(QPixmap.fromImage(self.image))

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self.label.pixmap())
        painter.drawImage(self.label.rect(), self.image, self.label.rect())
        painter.end()


def main():    
    app = QApplication(sys.argv)
    window = main_window()

    window.show()
  
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
