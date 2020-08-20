import cv2
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path)
    success, image = vidObj.read() 
    cv2.imwrite("frame%d.jpg" % 1, image) 
  

FrameCapture("/media/sachin/New Volume/project/manipal/manipal/upload/cut1.mp4") 