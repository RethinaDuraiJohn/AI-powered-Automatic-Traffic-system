# Object Detection
# Importing the libraries
import torch
from torch.autograd import Variable
import cv2
from .data import BaseTransform, VOC_CLASSES as labelmap
from .ssd import build_ssd

import os
basedir = os.path.abspath(os.path.dirname(__file__))
# ctdir = os.path.join(basedir, 'ssd/')
ctdir = os.path.join(basedir, 'ssd300_mAP_77.43_v2.pth')
print(ctdir)

# Creating the SSD neural network
net = build_ssd('test') # We create an object that is our neural network ssd.
net.load_state_dict(torch.load(ctdir, map_location = lambda storage, loc: storage)) # We get the weights of the neural network from another one that is pretrained (ssd300_mAP_77.43_v2.pth).

transform = BaseTransform(net.size, (104/256.0, 117/256.0, 123/256.0)) # We create an object of the BaseTransform class, a class that will do the required transformations so that the image can be the input of the neural network.


def getCount(num,frame):
    # frame = cv2.imread(filename)
    height, width, layers = frame.shape
    size = (width,height)
    count=0
    height, width = frame.shape[:2]
    frame_t = transform(frame)[0] # We apply the transformation to our frame.
    x = torch.from_numpy(frame_t).permute(2, 0, 1) # We convert the frame into a torch tensor.
    x = Variable(x.unsqueeze(0)) # We add a fake dimension corresponding to the batch.
    y = net(x) 
    detections = y.data
    scale = torch.Tensor([width, height, width, height]) # We create a tensor object of dimensions [width, height, width, height].

    #light,medium,heavey
    ans=[0,0,0]
    for i in range(detections.size(1)): # For every class:
        j = 0 
        while detections[0, i, j, 0] >= 0.25:
                bottomLeftCornerOfText = (10,100)   
                pt = (detections[0, i, j, 1:] * scale).numpy() 
                if i in (2,6,7,14):           
                    cv2.rectangle(frame, (int(pt[0]), int(pt[1])), (int(pt[2]), int(pt[3])), (255, 0, 0), 2) 
                    cv2.putText(frame, labelmap[i-1], (int(pt[0]), int(pt[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)# We put the label of the class right above the rectangle.
                    cv2.imwrite('final'+str(num)+'.jpg', frame) 
                    if i == 6 :
                        ans[2]+=1
                    if i == 7:
                        ans[1]+=1
                    if i == 14 or i==2:
                        ans[0]+=1
                j += 1 # We increment j to get to the next occurrence.
                #cv2.imwrite('classcheckop5.png',frame) 
    return ans    
