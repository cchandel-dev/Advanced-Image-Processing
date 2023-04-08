import numpy as np
from scipy.signal import convolve2d
from PIL import Image
import matplotlib.pyplot as plt
import os
import re

def compassKernels(direction = 'all'):
    mp = {
          'n':[[-3,-3, 5],[-3, 0, 5],[-3, -3, 5]], 
          'nw':[[-3, 5, 5],[-3, 0, 5],[-3, -3, -3]], 
          'w':[[5, 5, 5],[-3, 0, -3],[-3, -3, -3]], 
          'sw':[[5, 5, -3],[5, 0, -3],[-3, -3, -3]], 
          's':[[5, -3, -3],[5, 0, -3],[5, -3, -3]], 
          'se':[[-3, -3, -3],[5, 0, -3],[5, 5, -3]], 
          'e':[[-3, -3, -3],[-3, 0, -3],[5, 5, 5]], 
          'ne': [[-3, -3, -3],[-3, 0, 5],[-3, 5, 5]]
        }
    if direction not in mp.keys():
        return mp
    else:
        return mp[direction]

def angleImage(image, T = -1):
    angle_conversion = {'n': 0 , 'nw': 45, 'w': 90, 'sw': 135, 's':180, 'se':225, 'e':270, 'ne':315}
    kernels = compassKernels('all')
    gradients = {}
    for kernel in kernels.items():
        gradient = convolve2d(image, kernel[1], mode='same')
        gradients[kernel[0]] = gradient
    width = len(gradients['n'])
    height = len(gradients['n'][0])
    angle_image = [[0 for x in range(width)] for y in range(height)] 
    for i in range(width):
        for j in range(height):
            max_val = 0
            max_key = 'n'
            for grad in gradients.items():
                if grad[1][i][j] > max_val:
                    max_val = grad[1][i][j]
                    max_key = grad[0]
            angle_image[i][j] = angle_conversion[max_key]
    angle_image = np.array(angle_image)
    V = np.max(angle_image)
    if T >= 0:
        angle_image = np.where(angle_image >  round(T*V/45) * 45, V, 0)
    return angle_image

def magnitudeImage(image, T = -1):
    kernels = compassKernels('all')
    gradients = []
    for kernel in kernels.values():
        gradient = convolve2d(image, kernel, mode='same')
        np.absolute(gradient)#convert every gradient to absolute first
        gradients.append(gradient)
    width = len(gradients[0])
    height = len(gradients[0][0])
    magnitude_image = [[0 for x in range(width)] for y in range(height)]
    for i in range(width):
        for j in range(height):
            max_val = 0
            for grad in gradients:
                if grad[i][j] > max_val:
                    max_val = grad[i][j]
            magnitude_image[i][j] = max_val
    magnitude_image = np.array(magnitude_image)
    V = np.max(magnitude_image)
    if T >= 0 :
        magnitude_image = np.where(magnitude_image > T*V, V, 0)
    return magnitude_image

def is_numeric(s):
    regex = "^[-+]?\d*\.?\d+$"
    return bool(re.match(regex, s))

def compare_magnitude():
    # Get the absolute path of the current Python file
    file_path = os.path.abspath(__file__)
    # Get the path to the parent directory
    parent_dir = os.path.dirname(file_path)
    im = Image.open(os.path.join(parent_dir, 'testpattern512.tif'))
    img = np.array(im)
    fig, ax = plt.subplots(2,2)    
    plt.suptitle("Magnitude Images at Different Thresholds")
    for i in range(4):
        print(i)
        row = i // 2
        col = i % 2
        mag_im = magnitudeImage(img, i*0.25)
        ax[row, col].imshow(mag_im, cmap='gray')
        ax[row, col].set_title('Magnitude Image with {} threshold'.format(i*0.25))       
        ax[row, col].get_xaxis().set_visible(False)
        ax[row, col].get_yaxis().set_visible(False)

    # Show the figure
    fig = plt.get_current_fig_manager()
    fig.set_window_title("Comparing Magnitude Images")
    plt.show(block = True)

def main():
    # Get the absolute path of the current Python file
    file_path = os.path.abspath(__file__)
    # Get the path to the parent directory
    parent_dir = os.path.dirname(file_path)
    im = Image.open(os.path.join(parent_dir, 'testpattern512.tif'))
    imarray = np.array(im)

    fig, ax = plt.subplots(1, 2)

    # Set the threshold percentages
    angle_threshold = -1
    magnitude_threshold = -1
    while angle_threshold < 0 :
        user_input = input("Enter an angle image threshold which is a float between 0 and 1 (not-inclusive): ")
        if is_numeric(user_input):
            angle_threshold = float(user_input)
            if angle_threshold > 1:
                angle_threshold = 0.99
    while magnitude_threshold < 0:
        user_input = input("Enter a magnitude image threshold which is a float between 0 and 1 (not-inclusive): ")
        if is_numeric(user_input):
            magnitude_threshold = float(user_input)
            if magnitude_threshold > 1:
                magnitude_threshold = 0.99

    #Display the Images
    ax[0].imshow(angleImage(im, angle_threshold), cmap='gray')
    ax[0].set_title('Angle Image with {} threshold'.format(angle_threshold))
    ax[1].imshow(magnitudeImage(im, magnitude_threshold), cmap='gray')
    ax[1].set_title('Magnitude Image with {} threshold'.format(magnitude_threshold))

    #customize axes
    ax[0].get_xaxis().set_visible(False)
    ax[0].get_yaxis().set_visible(False)
    ax[1].get_xaxis().set_visible(False)
    ax[1].get_yaxis().set_visible(False)

    # Show the figure
    fig = plt.get_current_fig_manager()
    fig.suptitle("Kirsh Angle and Magnitude Images")
    fig.set_window_title("Kirch Compass Images")
    plt.show(block = True)

if __name__ =='__main__':
    compare_magnitude()