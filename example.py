
from gimpysolver import captchaSolverRPA #

import PIL
import os
import cv2
import matplotlib.pyplot as plt

path_imgTest = './test_images/' # Test Folder with images

# testing with Images right dimension
import random
list_img = os.listdir(path_imgTest)
lst = random.choices(list_img,k=15)

for img_ in lst:
    # Create the object
    captcha = captchaSolverRPA.captcha_solver(path_imgTest+img_)

    # Veridy if image have Dimention correctly
    if captcha.wrongDimension:
	# With this method resize and rewrite the img with right dimension
        captcha.resize()
    image = PIL.Image.open(path_imgTest+img_)
    
    img=cv2.imread(path_imgTest+img_,cv2.IMREAD_GRAYSCALE)
    plt.imshow(img, cmap=plt.get_cmap('gray'))
    plt.show()
    
    
    print(img_)
    print(captcha.predict())




