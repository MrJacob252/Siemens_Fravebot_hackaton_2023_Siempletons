import camera_client as cc
import cv2

if __name__ == "__main__":
    img = cc.stream_video()
    
    cv2.imshow("mrtka",img)
    cv2.waitKey(0)
    
        
    