#!/usr/bin/python
#Dialog_window.py
from menu_data_items import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess as sp

class Dialog_window(QDialog):

        def __init__(self, parent = None):
                QDialog.__init__(self, parent)
                self.initUI()

        def initUI(self):
                dict1 = {}
                fbox = QFormLayout()
                self.lbl1 = QLabel("Source File")
                self.le1 = QLineEdit()
#                self.le1.setText("self.showdialog")
#                dict1['3'] =  self.le1.text()
#                print dict1['3']
                self.bttn1 = QPushButton("Browse...")
                fbox.addRow(self.lbl1)
                fbox.addRow(self.le1,self.bttn1)
                self.bttn1.clicked.connect(self.get_file_name_and_put_combo_data)
                ###################################
                self.lbl2 = QLabel("Function Name")
                self.cbx2 = QComboBox()
                fbox.addRow(self.lbl2)
                fbox.addRow(self.cbx2)
                ##################################
                self.lbl3 = QLabel("Tool Name")
                self.le3 = QLineEdit()
                fbox.addRow(self.lbl3)
                fbox.addRow(self.le3)
                ##################################
                self.lbl4 = QLabel("Icon Image")
                self.le4 = QLineEdit()
                self.bttn4 = QPushButton("Browse...")
                self.bttn4.resize(self.bttn4.sizeHint())
                fbox.addRow(self.lbl4)
                fbox.addRow(self.le4,self.bttn4)
                self.bttn4.clicked.connect(self.get_image_name)
                ################################
                self.lbl5 = QLabel("Shortcut Key")
                self.le5 = MyLineEdit()
                self.bttn5 = QPushButton("Grab Shortcut...")
                fbox.addRow(self.lbl5)
                fbox.addRow(self.le5,self.bttn5)
                self.le5.setEnabled(False)
                self.bttn5.clicked.connect(self.enable_lineEdit)
                self.le5.keyPressed.connect(self.update)
                self.le5.disableLineEdit.connect(self.disable_lineEdit )
                ################################
                self.lbl6 = QLabel("Tool Description")
                self.le6 = QLineEdit()
                fbox.addRow(self.lbl6)
                fbox.addRow(self.le6)
                ################################
                self.lbl7 = QLabel("Menu Location")
                self.le7 = QLineEdit()
                fbox.addRow(self.lbl7)
                fbox.addRow(self.le7,)
                ###############################
                self.bttnCancel = QPushButton("CANCEL")
                self.bttnAccept = QPushButton("ACCEPT")
                self.bttnAccept.clicked.connect(
                                self.from_dialog_win_put_data_into_files)
                self.bttnCancel.clicked.connect(self.close)
                fbox.addRow(self.bttnCancel,self.bttnAccept)
                ##############################
                self.setLayout(fbox)
                self.setWindowTitle("Create Plugin")
            
#                self.show()
        def from_dialog_win_put_data_into_files(self):
                my_func_path = get_path_basename(self.le1.text())
                #module_name =  my_func_path[0:len( my_func_path)-3]
                module_name =  my_func_path.replace(".py","")
                file1 = open("my_functions.py", "a")
                file1.write("\nfrom  " + module_name + " import *")
                file1.close()
                file1 = open('menu_data_items.py', "a")
                #file1.write('/n' + "dict" ) 
                if len(main_dict) == 0 :
                        tmp_dict = 'my_dict' + str(len(main_dict)  )
                else :
                        tmp_dict = 'my_dict' + str(len(main_dict) + 1)
                file1.write("\n"+

                     tmp_dict+" =  {\n           1 : '"
                                      + str(self.cbx2.currentText()) +
                                "',\n           2 : '"+ self.le3.text() + 
                                "',\n           3 : '"+ self.le4.text() +
                                "',\n           4 : '"+ self.le5.text() +
                                "',\n           5 : '"+ self.le6.text() +
                                "',\n           6 : '"+ self.le7.text() + "'}"+
                      "\nmain_dict.update( {" + str(len(main_dict)) + " : " +
                                                             tmp_dict + "} )")
                self.close()


        def get_file_name_and_put_combo_data(self):

                fname = QFileDialog(self)
                fname.setFileMode(1)
                fname.setLabelText( fname.Accept, "Import" )
                fname.setNameFilter("Files (*.py )")
                if (fname.exec_()):
                        file_name = fname.selectedFiles()
                else : file_name = ['']
                self.le1.setText(file_name[0])
                if file_name[0] != "" :
                        self.get_func_names_for_combobox(file_name[0])
        def get_image_name(self):

                fname = QFileDialog(self)
                fname.setFileMode(1)
                fname.setLabelText( fname.Accept, "Import" )
                fname.setNameFilter("Images (*.png *.xpm *.jpg)")
                if (fname.exec_()):
                        file_name = fname.selectedFiles()
                self.le4.setText(file_name[0])
        def get_func_names_for_combobox(self,file_name):
                file_name = str(file_name)
                args = ["awk", r'/^\s*def/ { print $2}',file_name ]
                p = sp.Popen(args, stdin = sp.PIPE,
                             stdout = sp.PIPE, stderr = sp.PIPE )
                str1 = p.stdout.read()
                list1 = str1.splitlines()
                list2 = []
                self.cbx2.clear()
                for i in  list1 :
                        str2 = i[:i.find('(')]
                        self.cbx2.addItem(str2)
 
        ########### update is called by keyPressed
        ########### signal from MyLineEdit class
        def update(self, text):
                self.le5.setText(text)
        def enable_lineEdit (self):
                self.le5.setEnabled(True)
                self.le5.setText("")
                self.le5.setFocus(True)
        ########## disable_lineEdit is called 
        ########## by disableLineEdit signal from MyLineEdit class
        def disable_lineEdit (self,disable):
                self.le5.setEnabled(disable)
#########################
def get_path_basename(string):
        list1 = string.split("/")
        return list1[-1]
########################

MOD_MASK = (Qt.CTRL | Qt.ALT | Qt.SHIFT | Qt.META)

class MyLineEdit(QLineEdit):
    keyPressed = pyqtSignal(str)
    disableLineEdit = pyqtSignal(bool)

    def keyPressEvent(self, event):
        keyname = ''
        key = event.key()
        modifiers = int(event.modifiers())
        if (modifiers and modifiers & MOD_MASK == modifiers and
            key > 0 and key != Qt.Key_Shift and key != Qt.Key_Alt and
            key != Qt.Key_Control and key != Qt.Key_Meta):

            keyname = QKeySequence(modifiers + key).toString()

            print('event.text(): %r' % event.text())
            print('event.key(): %d, %#x, %s' % (key, key, keyname))
            self.disableLineEdit.emit(False)
        self.keyPressed.emit(keyname)
