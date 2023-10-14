import cv2
import numpy as np

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

def image_shenanigans(image):
    
    img = np.asarray(image)
    
    img = image_resize(img, width=400)
    
    # convert to HSV and extract saturation channel
    # sat = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2HSV)[:, :, 1]
    sat = cv2.cvtColor(img.copy(), cv2.COLOR_RGB2GRAY)
    sat = cv2.GaussianBlur(sat, (9, 9), 0)
    
    
    ret, thresh = cv2.threshold(sat, 90, 150, 0)
    
    # apply morphology close to fill interior regions in mask
    # kernel = np.ones((29, 29), np.uint8)
    # morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # kernel = np.ones((31, 31), np.uint8)
    # morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel) 
    
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    # print('# # # # # TYPES # # # #')
    # print(type(contours))
    # print(type(hierarchy))
    
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    cv2.imshow('test',img)
    # cv2.waitKey(0)
    
    
    
    
if __name__ == '__main__':
    im = cv2.imread('test0.jpg')
    # im = np.asarray(im)
    # cv2.imshow('test', im)
    # cv2.waitKey(0)
    
    image_shenanigans(im)
    