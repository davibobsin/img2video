import cv2
import os
import glob
import argparse

parser = argparse.ArgumentParser(description='Create Video from images.')

parser.add_argument('-i','--in',help='Input string with % as variable.',required=True)
parser.add_argument('-o','--out', help='Output video name with ext.')
parser.add_argument('-f','--framerate',help='Frame rate of the video.')

args=vars(parser.parse_args())
out = 'video.avi'
fr = 1
if(args['out']!=None):
	out = args['out']
if(args['framerate']!=None):
	fr = args['framerate']
print('OUTPUT NAME: '+out)
print('FRAME RATE: '+str(fr))

st = args['in'].split('%')
pre,post = st[0],st[1]

print(pre)
print(post)

i = 0
frame = cv2.imread(pre+str(i)+post)
height,width,layers = frame.shape

video = cv2.VideoWriter(out,0,fr,(width,height))

while(os.path.isfile(pre+str(i)+post)):
	video.write(cv2.imread(pre+str(i)+post))

video.release()
