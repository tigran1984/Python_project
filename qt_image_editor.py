#!/usr/bin/python
################### menu and toolbar initialiation data
from menu_data_items import *
################## functions which is called from menu or toolbar
from my_functions  import * 
################# The dialog window for creating functions
from Dialog_window import Dialog_window
################# image bluring files
from Gaussian_matrix import Gaussian_matrix
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Main_Window( QMainWindow):
        for i in range(len(main_dict)):
                exec("def func"+str(i)+"(self):\
                \n\t\t\t\t\
                        self."+main_dict[i][1]+"="+main_dict[i][1]+"(self)\
                \n\t\t\t\t\
                        return self."+main_dict[i][1])

        def __init__(self, parent = None):
                super(Main_Window,self).__init__(parent)
                self.initUI()

        def initUI(self):
                self.statusBar()
                self.label = QLabel()
                self.setCentralWidget(self.label)
                menubar = self.menuBar()
                toolbar = self.addToolBar('')
                action1 = QAction( 'Create Plugin', self)
                action1.triggered.connect(self.showdialog)
                action1.setShortcut("Ctrl+Shift+C")
                fileMenu = menubar.addMenu("New Plugin")
                fileMenu.addAction(action1)
                toolbar.addAction(QIcon("plugin0.png"),'',self.showdialog)
                check_menu_dict = {} 
                set_func_dict = {}
                dic = main_dict
                for i in range(len(dic)):
                        exec("act"+str(i)+"=QAction(dic[i][2],self)")
                        exec("act"+str(i)+".triggered.connect(\
                              self.func"+str(i)+")")
                        exec("act"+str(i)+".setShortcut('"+dic[i][4]+"')")
                        exec("act"+str(i)+".setStatusTip('"+dic[i][5]+"')")
                        if ((dic[i][6] in check_menu_dict.values()) == False  ):
                                exec(dic[i][6] +" =menubar.addMenu(\
                                     '"+dic[i][6]+"')")
                                check_menu_dict.update({str(len(\
                                     check_menu_dict)): dic[i][6]})
                        exec("def func"+str(i)+"(self):\n\tself."+\
                                dic[i][1]+"="+\
                                dic[i][1]+"\n\treturn self"+dic[i][1])
                        exec(dic[i][6] +".addAction(act"+str(i)+")")
                        if dic[i][3] == "" :
                                exec("toolbar.addAction('"+dic[i][2]+\
                                        "',self.func"+str(i)+")")
                        else :
                                exec("toolbar.addAction(QIcon('"+dic[i][3]+\
                                     "'),'',self.func"+str(i)+")")
                self.setWindowTitle('Menubar')    
                self.show()
    
        def showdialog(self):
                d = Dialog_window()
                d.exec_()
        
        def convert_string_to_func_name(self,string_my_func):
                func = 'return_func_name'
                exec(func + " =" + string_my_func)
                return return_func_name
        
        def enter_blur_radius(self):
                text, ok = QInputDialog.getText(self, 'Blur Radius', 
                        'Enter blur radius:')
                if ok:
                        self.le.setText(str(text))

def main():
    
    app = QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())
                             
if __name__ == '__main__':
    main()    
        
