import cv2 as cv 
import numpy as np 
import itertools

from os import listdir
from os.path import isfile, join

images_folder = "images/"
results_folder = "results/"

kernel_1 = np.full((1,1),255)
kernel_3 = np.full((3,3),255)
kernel_5 = np.full((5,5),255)
kernel_7 = np.full((7,7),255)
kernel_9 = np.full((9,9),255)
kernel_11 = np.full((11,11),255)


def erosion(img, kernel):
   
    new_img = np.zeros(img.shape)
    
    y_k, x_k = kernel.shape
    y_img, x_img = img.shape
    
    for y, x in itertools.product(range(y_img-y_k), range(x_img-x_k)):
         
        sub_img = img[y : y + y_k, x : x + x_k]
        if np.array_equal(sub_img, kernel):
            new_img[y + int(y_k/2), x+ int(x_k/2)] = 1
        
    return new_img*255

def dilation(img, kernel):
    
    y_k, x_k = kernel.shape
    y_img, x_img = img.shape
    
    new_img = img.copy()
    
    for y, x in itertools.product(range(y_img-y_k), range(x_img-x_k)):
        
        sub_pixel = img[y + int(y_k/2), x + int(x_k/2)]
        
        if sub_pixel == 255:
            new_img[y : y + y_k, x : x + x_k] = np.ones(kernel.shape) 
                
        
    return new_img * 255
    


def opening(img, SE):
    
    img = erosion(img,SE)
    
    img = dilation(img, SE)
    
    return img 
    

def closing(img, SE):
    
    img = dilation(img, SE)
    
    img = erosion(img, SE)
    
    return img 
    
def boundary(img):
    
    kernel = np.full((3,3), 255)
    y_k, x_k = kernel.shape
    y_img, x_img = img.shape
    
    new_img = np.zeros(img.shape)
    
    for y, x in itertools.product(range(y_img-y_k), range(x_img-x_k)):
        
        sub_img = img[y : y + y_k, x : x + x_k]
        
        if (sub_img[int(y_k/2), int(x_k/2)] == 255
                and not np.array_equal(sub_img, kernel)):
            
            new_img[y + int(y_k/2), x + int(x_k/2)] = 1
        
    return new_img*255
    

def main() :
    
    #Read in the pictures from absolute path above
    image_files_list = [f for f in listdir(images_folder) if isfile(join(images_folder, f))]
    for image_file in image_files_list:
        path_to_image = str(images_folder + image_file)
        
        img = cv.imread(path_to_image, 0)
        cv.imshow('normal/' + path_to_image, img)
        
        img = dilation(img, kernel_11)
        cv.imshow("dilated/" + path_to_image, img)
        
        img = erosion(img, kernel_5)
        cv.imshow('eroded/' + path_to_image, img)
        
        img = boundary(img)
        cv.imshow('border/' + path_to_image, img)
 
    
    key = cv.waitKey(0)
    
    if key == 27 or key == 'q':
        cv.destroyAllWindows()       
        

if __name__ == "__main__":
    main()
