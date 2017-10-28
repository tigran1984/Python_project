#!/usr/bin/python

from math import exp

class Gaussian_matrix():
        """ Createing and returning Gaussian matrix """
        def __init__(self,kernel_radius):
                #kernel_height, kernel_width = n x n 
                sigma = kernel_radius/2. # for [-2*sigma, 2*sigma]
                # compute the actual kernel elements
                hkernel = [self.gaussian_func(x, kernel_radius, sigma) for x in range(2*kernel_radius+1)]
                vkernel = [x for x in hkernel]
                kernel2d = [[xh*xv for xh in hkernel] for xv in vkernel]
                
                # normalize the kernel elements
                kernelsum = sum([sum(row) for row in kernel2d])
                kernel2d = [[x/kernelsum for x in row] for row in kernel2d]
                self.matrix = kernel2d           
        def gaussian_func(self,x, kernel_radius, sigma):

                return exp( -(((x-kernel_radius)/(sigma))**2)/2.0 )
        def get_matrix(self):

            return self.matrix

if __name__ =="__main__":
        matrix = Gaussian_matrix(1)
        print matrix.get_matrix()


