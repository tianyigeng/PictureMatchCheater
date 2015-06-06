import numpy as np
import pylab
import mahotas as mh
import search 
import image_split as split
import UI
import time

"""
f = open('sample.txt','w')
for i in range(len(label)):
    f.write(' '.join(str(x) for x in label[i])+'\n')
pylab.show()

"""

count = 0
while count <6:
    count+=1
    RECT =UI.getOrigin()
    pic = UI.getPic(RECT)
    #pic.save("screenshot.png")

    #image = mh.imread('screenshot.png')
    image = np.array(pic)
    #mg stands for "matching game"
    position,info = split.locate(image)
    print position
    print info
   
    label = split.split(image,position,info)
    [click,board,success] = search.solve(label)
    num_click = 0
    for (x,y) in click:
        UI.click((RECT[0] + position[2]+(2*y-1)*info[1]/2,RECT[1] + position[0]+(2*x-1)*info[0]/2))
        num_click+=1
        time.sleep(0.05)
        if num_click%2==0:
            time.sleep(0.2)
    if success:
        break
    for i in range(3):
        time.sleep(0.5)
        UI.click((RECT[0] + (position[2]+position[3])/2,RECT[1] + (position[0]+position[1]-info[0])/2))