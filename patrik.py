# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2
import os

def find_marker(image):
    image = np.asarray(image)
    image = image_resize(image, height=960)
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0) #5 5 0
    # cv2.imshow('s',gray)
    t_lower = 35 # Lower Threshold 
    t_upper = 100 # Upper threshold 
    # aperture_size = 5 # Aperture size 
    # L2Gradient = True # Boolean 
    edged = cv2.Canny(gray, t_lower, t_upper) #original values 35 125
    cv2.imshow('ss', edged)
    # cv2.waitKey(0)

    # ret, edged = cv2.threshold(gray, 0, 255, 
    #                         cv2.THRESH_BINARY_INV +
    #                         cv2.THRESH_OTSU) 
    # cv2.imshow('image', edged) 
    # cv2.waitKey(0)
    ################## MORPHOLOGICAL ELIPSING? ###########################
    # use morphology to close figure
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15)) #35 35 
    morph = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel, )
    cv2.imshow('morph',morph)
    ################## MORPHOLOGICAL CLOSING + DILATE ##################
    # Noise removal using Morphological 
    # closing operation 
    # kernel = np.ones((3, 3), np.uint8) 
    # closing = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, 
    #                             kernel, iterations = 2) 
    
    # # Background area using Dilation 
    # bg = cv2.dilate(closing, kernel, iterations = 1) 
    
    # # Finding foreground area 
    # dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0) 
    # ret, fg = cv2.threshold(dist_transform, 0.02
    #                         * dist_transform.max(), 255, 0) 
    
    # cv2.imshow('image', fg) 
    ########################################################################
    # cv2.waitKey(0)
    # # find the contours in the edged image and keep the largest one;
    # # we'll assume that this is our piece of paper in the image
    # cnts, hie = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   
    # image_copy = image.copy()
    # #####
    # i = 0
    # for contour in cnts: 
    
    #     # here we are ignoring first counter because  
    #     # findcontour function detects whole image as shape 
    #     if i == 0: 
    #         i = 1
    #         continue
    
    #     # cv2.approxPloyDP() function to approximate the shape 
    #     approx = cv2.approxPolyDP( 
    #         contour, 0.01 * cv2.arcLength(contour, True), True) 
        
    #     # # using drawContours() function to see what contours are on image
    #     # cv2.drawContours(im1, [contour], 0, (0, 0, 255), 5) 
        
    #     # if len(approx) != 4:
    #     #     continue
        
    #     # finding center point of shape 
    #     M = cv2.moments(contour) 

    #     # print(M['m00'])

    #     if M['m00']<300:  #original was m00
    #         continue

    #     # using drawContours() function 
    #     cv2.drawContours(image_copy, [contour], 0, (0, 0, 255), 5) 

    #     if M['m00'] != 0.0: 
    #         x = int(M['m10']/M['m00']) 
    #         y = int(M['m01']/M['m00']) 

    #     # print(M['m00'])
    #     # print(M)
    #     cv2.drawContours(image=image_copy, contours=cnts, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    # ######
    # # cv2.imshow('None approximation', image_copy)
    # # cv2.waitKey(0)
    
    # cnts = imutils.grab_contours(cnts)
    
    # c = max(cnts, key = cv2.contourArea)
    # rect = cv2.minAreaRect(c)
    # box = cv2.boxPoints(rect)
    # box = np.int0(box)
    # image = cv2.rectangle(image, box[0], box[3],color=(255, 0, 0),thickness=2) 
    # # cv2.imshow('x',image)
    # # cv2.waitKey(0)
    # # compute the bounding box of the of the paper region and return it
    # return image,1 #cv2.minAreaRect(c)

def image_resize(image: np.ndarray, width = None, height = None, inter = cv2.INTER_AREA):
    '''
    Resize image while keeping it's aspect ratio
    '''
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized


if __name__ == '__main__':
    path = ('./img/')

    files = os.listdir(path)

    print(files)

    # for file in files:
    im = cv2.imread(path+files[7]) #-3
    im = np.asarray(im)
    im = image_resize(im,width=1920)
    cv2.imshow('skap',im)
    cv2.waitKey(0)
    print("======================")
    print(find_marker(im))


# break


