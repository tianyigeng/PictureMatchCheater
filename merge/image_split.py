import numpy as np
import pylab
import mahotas as mh
import types

# constants
upper_distance = 100  #the start searching 
approxWidth = 40
threshold = 300
border = 1

def pre_process(image):
    """
    
    return black_white image, given a colorful image as input.        
    """
    T = mh.thresholding.otsu(image)
    image = image > T
    image = image[::,::,0]+image[::,::,1]+image[::,::,2]
    image = image.reshape(image.shape[0],-1)
    image = image >0
    pylab.figure(1)
    pylab.imshow(image)
    return  image 

def locate(image):
    """ 
    
    Given an numpy.array as input, return the position of the matching game
    as well as the size of the game(num_x,num_y) 
    and the size of each grids(size_x,size_y).        
    """
    image = pre_process(image)    
    height,width = image.shape
    
    # stop going down when a grid is found
    up = upper_distance
    num_white = np.sum(image,axis = 1) 
    while num_white[up]-num_white[up-1]<=(approxWidth/2):    
        up +=1
    
    # stop going up when a grid is found
    down = height-2
    while num_white[down]-num_white[down+1]<=(approxWidth/2):
        down -=1
                
    current_image = image[up:]          
    """cut the top part(including the time bar, all sorts of buttons) away 
    which will interfere with our searching process"""    
    c_height,c_width = current_image.shape
    
        # stop going right when a grid is found    
    num_white = np.sum(current_image,axis =0)
    left = 1
    while num_white[left]-num_white[left-1]<=(approxWidth/2):
        left +=1
        
    # stop going left when a grid is found    
    right = c_width-2
    while num_white[right]-num_white[right+1]<=(approxWidth/2):
        right -=1
       
    current_image = current_image[:down+1-up,left:right+1]
    height,width = current_image.shape
    pylab.figure(2)
    pylab.imshow(current_image)
    

    num_white = np.sum(current_image,axis = 1)
    divd_x = [i for i in range(height) if num_white[i]< approxWidth/2]
    divd_x = [divd_x[i] for i in range(len(divd_x)) if ((i==0) or (i==len(divd_x)-1)) or not (divd_x[i-1]+1==divd_x[i] and divd_x[i+1]-1==divd_x[i])]
    # only keep the truly dividing lines, namely  those marginal lines. 
    
    num_white = np.sum(current_image,axis = 0)
    divd_y = [j for j in range(width) if num_white[j]< approxWidth/2]
    divd_y = [divd_y[i] for i in range(len(divd_y)) if ((i==0) or (i==len(divd_y)-1)) or not (divd_y[i-1]+1==divd_y[i] and divd_y[i+1]-1==divd_y[i])]
    # only keep the truly dividing lines, namely  those marginal lines. 
    
    
    """ 
    This part needs further refinement.
    """
    if len(divd_x):
        size_x = divd_x[0]
        num_x = divd_x[-1] / size_x +1
    else:
        size_x = height - 1
        num_x = 1
        
    if len(divd_y):
        size_y = divd_y[0]
        num_y = divd_y[-1] / size_y +1
    else:
        size_y = height - 1
        num_y = 1
        
    position = (up,down,left,right)
    info = (size_x,size_y,num_x,num_y)
    
    return  position, info 
       
    
def split(image,position,info):
    """
    
    Return a 2d matrix label, which labels different kinds of grids using natural numbers.
    (By convention, the empty grid is labeled 0)
        
    """
    size_x, size_y, num_x, num_y = info
    up, down, left, right = position
    
    image = image[up:down+1,left:right+1]
    T = mh.thresholding.otsu(image)
    image = image >T
    pylab.figure(3)
    pylab.imshow(image)
    #pylab.show()    
   
    game = [[0]* num_y for j in range(num_x)]
    for i in range(num_x):
        for j in range(num_y):
            game[i][j] = image[i*(size_x+1):(i+1)*(size_x+1)-1,j*(size_y+1):(j+1)*(size_y+1)-1]
    
    '''for row in game:
        print [grid.shape for grid in row]'''
    # using a quite naive method -- calculating the statistical distance between two grids
    # improvement is needed here, to speed up the program
    black = np.array([[[0]*3]*size_y]*size_x)
    records = [black]
    label = [[0]* num_y for j in range(num_x)]
    for i in range(num_x):
        for j in range(num_y):
            find = False
            for index in range(len(records)):
                if distance(records[index],game[i][j])< threshold:
                    label[i][j] = index 
                    find =True
                    break
            if not find:            
                records.append(game[i][j])
                label[i][j] = len(records)-1
    return label
    
def distance(a1,a2):
    """
    
    calculate the distance between a1 and a2  
    """
    if (a1.shape!=a2.shape): 
         return    
    dis = np.sum(np.abs(a1-a2))
    return dis