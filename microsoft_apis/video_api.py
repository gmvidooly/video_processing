import numpy as np
import cv2
import sys

video = cv2.VideoCapture(sys.argv[1])
framerate = video.get(cv2.cv.CV_CAP_PROP_FPS)
framecount = 0
count = 0
while(True):
	# Capture frame-by-frame
    success, image = video.read()

    framecount += 1
    # Check if this is the frame closest to 10 seconds
    if (framecount == int(framerate) * (count +1)):
        print success, int(framerate)
        framecont = 0
        count += 1
        # proxy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('image%d.png'%(count),image)

    # Check end of video
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    if success:
        continue
    else:
        break
	# proxy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# cv2.imwrite('image.png', proxy)

# When everything done, release the capture
video.release()