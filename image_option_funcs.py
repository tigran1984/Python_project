
from PyQt4.QtGui import *
from PyQt4.QtCore import *



def save_image(self):
        formats = QImageWriter.supportedImageFormats()
        print formats
        formats = map(lambda suffix: u"*."+unicode(suffix), formats)
        path = unicode(QFileDialog.getSaveFileName(self, self.tr("Save Image"),
                "", self.tr("Image files (%1)").arg(u" ".join(formats))))
#    path = QFileDialog.getSaveFileName(self, self.tr("Save Image"),\
#                "", self.tr("Images (*.png *.xpm *.jpg)"))
        
        if path:
                if not self.label.pixmap().save(path):
                        QMessageBox.warning(self, self.tr("Save Image"),
                        self.tr("Save is Failed\n may be unsported image type "))
                else :
                        QMessageBox.information(self, self.tr("Save Image"),
                        self.tr("Successfully Saved"))
        
def load_image(self):
        fname = QFileDialog()
        fname.setFileMode(1)
        fname.setLabelText( fname.Accept, "Import" )
        fname.setNameFilter("Images (*.png *.xpm *.jpg)")
        file_name = [""]
        if (fname.exec_()):
                file_name = fname.selectedFiles()
                if file_name[0] != "": 
                        self.image = QImage(file_name[0])
                        self.image_copy = QImage(file_name[0])
                        self.label.setPixmap(
                              QPixmap.fromImage(self.image))
