import cv2
import os

# Opens the Video file
videocap= cv2.VideoCapture('.../xyz.mp4')

#create a folder to place frames of the video
try:
    if not os.path.exists('.../videoframes'):
        os.makedirs('.../videoframes')
except OSError:
    print ('Error: Creating directory of data')

#slide number
slide = 0
#videocap.read() nextframe existing is equal to True to run the loop
nxtframe = 1
while(nxtframe):
    nxtframe, frame = videocap.read()
    videoname = '.../videoframes/socialdist' + str(slide) + '.jpg'
    #create frame and place it in videoname path with the frame name as intialized above
    cv2.imwrite(videoname, frame)
    print ('Creating...' + videoname)
    slide+=1


videocap.release()
cv2.destroyAllWindows()
