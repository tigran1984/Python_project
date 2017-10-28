#!/usr/bin/python
from Gaussian_matrix import Gaussian_matrix
from progressbar import  ProgBar
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

def blur_picture(obj):
    
        def blur_effect(x,y,radius):
            countRed,countGreen,countBlue = 0,0,0
            mtx = Gaussian_matrix(radius)
            kernel_matrix = mtx.get_matrix()
            for i,m in zip (range(x-radius, x+radius+1),range(radius*2+1 )):
                for j,n in zip (range(y-radius, y+radius+1),range(radius*2+1 )):
                    if obj.image.valid(i,j):
                        color = obj.image.pixel(i,j)
                        countRed   += QColor(color).red()*kernel_matrix[m][n]
                        countGreen += QColor(color).green()*kernel_matrix[m][n]
                        countBlue  += QColor(color).blue()*kernel_matrix[m][n]
                   
            red_v   = countRed   # / ((radius*2 + 1)*(radius*2 + 1))
            green_v = countGreen # / ((radius*2 + 1)*(radius*2 + 1))
            blue_v  = countBlue  # / ((radius*2 + 1)*(radius*2 + 1))
            return [red_v,green_v, blue_v]
        h = obj.image.height()
        w = obj.image.width()
        text, ok = QInputDialog.getText(obj, 'Input Dialog', 
                    'Enter Radius Value:')
        if ok :
                radius = int(text)
        else:
                return
        pbar = QProgressBar()
        pbar.setMinimum(1)
        pbar.setMaximum(w-1)
        obj.statusBar().addWidget(pbar)
        for x in range(0, w - 1):
            for y in range(0, h - 1):
                color_list = blur_effect(x,y,radius)
                obj.image_copy.setPixel(QPoint(x,y) ,qRgb(  color_list[0], color_list[1], color_list[2]))
            pbar.setValue(x)
        obj.statusBar().removeWidget(pbar)
        #obj.repaint(obj.rect())

        obj.label.setPixmap(QPixmap.fromImage(obj.image_copy))

def sharpen_picture(obj):

        def sharpen_effect(x,y,radius = 1):

            def set_corect_value(value):
                if value > 255 :
                    value = 255
                elif value < 0 :
                    value = 0
                return value
                
            radius = 1
            countRed,countGreen,countBlue = 0,0,0
            kernel_matrix = [[-1,-1,-1],
                             [-1,9,-1], 
                             [-1,-1,-1]] 
            for i,m in zip (range(x-radius, x+radius+1),range(radius*2+1 )):
                for j,n in zip (range(y-radius, y+radius+1),range(radius*2+1 )):
                    if obj.image.valid(i,j):
                        color = obj.image.pixel(i,j)
                        countRed   += QColor(color).red()*kernel_matrix[m][n]
                        countGreen += QColor(color).green()*kernel_matrix[m][n]
                        countBlue  += QColor(color).blue()*kernel_matrix[m][n]
                   
            red_v   = set_corect_value(countRed) 
            green_v = set_corect_value(countGreen)  
            blue_v  = set_corect_value(countBlue) 
            return [red_v,green_v, blue_v]
        h = obj.image.height()
        w = obj.image.width()
        radius  = 1 
        #pBar = ProgBar(0,w-1)
        #pBar.exec_
        pbar = QProgressBar()
        pbar.setMinimum(1)
        pbar.setMaximum(w-1)
        obj.statusBar().addWidget(pbar)
        for x in range(0, w - 1):
            for y in range(0, h - 1):
                color_list = sharpen_effect(x,y,radius)
                obj.image_copy.setPixel(QPoint(x,y) ,qRgb(  color_list[0], color_list[1], color_list[2]))
            pbar.setValue(x)
        obj.statusBar().removeWidget(pbar)
        
       # obj.update(obj.rect())


        obj.label.setPixmap(QPixmap.fromImage(obj.image_copy))
