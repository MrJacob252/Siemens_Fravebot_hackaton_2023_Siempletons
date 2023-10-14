import cv2
# import matplotlib.pyplot as plt
import numpy as np


def main(img):
    # cap = cv2.VideoCapture(0)
    # cap.set(3,1280)
    # cap.set(4,720)
    #cap.set(10,70)

    s_image = 640*480

    classNames= []
    classFile = 'coco.names'
    with open(classFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    # print(classNames)

    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(False)

    thres = 0.5
    # 0.4
    conditionmet = False

    # while True:
        # success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)
    print(classIds,bbox)

    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
            cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            npbbox = np.array(bbox)
            s_objects = max(abs(npbbox[:,2] - npbbox[:,0]) * (npbbox[:,3]-npbbox[:,1]))
            if s_objects > 0.3*s_image:
                conditionmet = True
            # for x in range(classIds[0]):
            #     s_object = abs(bbox[x][0] - bbox[x][2])*abs(bbox[x][1]-bbox[x][3]) 
            #     print(s_object)
            #     if s_object > 0.3*s_image:
            #         conditionmet = True
    cv2.imshow('Output',img)
    cv2.waitKey(1)

    if conditionmet:
        return True
    return False


    
    


        # if cap.isOpened():
        #     ret, frame = cap.read()
        # else:
        #     ret = False

        # # img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # img1 = frame

        # classIds, confs, bbox = net.detect(img1,confThreshold=0.7)
        # print(classIds,bbox)

    # if len(classIds) != 0:
    #     for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
    #         cv2.rectangle(img1,box,color=(0,255,0),thickness=2)
    #         # cv2.putText(img1,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
    #         # cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    #         cv2.putText(img1,classNames[classId-1],(box[0],box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    #         cv2.putText(img1,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
    #         cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    # while True:
    #     cv2.imshow('Output',img1)
    #     cv2.waitKey(5000)

    #     # plt.imshow(img1)
    #     # plt.title('Skap')
    #     # plt.xticks([])
    #     # plt.yticks([])
    #     # plt.show()

    #     cap.release()
    


if __name__ == '__main__':
    main()
    print(cv2.__version__)

    print('ahojda')