import cv2
import os
path = 'Images'
Images=[]
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()== False):
    print("Unable to read the feed")
height =int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

if ext in ['.gif','.png','.jpg','jpeg','jfif']:
    file_name =path+"/"+file
    print(file_name) 

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0, count-1):
cv2.imread()
out.write()

