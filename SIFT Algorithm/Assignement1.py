import os
import cv2
import subprocess
#load image dataset from input file
directory = "input"
images = []
for filename in os.listdir(directory):
    # load the image file using opencv
    img = cv2.imread(os.path.join(directory, filename))
    # append the image to the list
    images.append(img)

#PATH 1
#run image dataset through sift feature extractor
i = 0
for image in images:
    subprocess.run(["python3.10", "Sift.py", i])
    i+=1

#load image dataset from output file
directory = "output"
siftimages = []
for filename in os.listdir(directory):
    # load the image file using opencv
    img = cv2.imread(os.path.join(directory, filename))
    # append the image to the list
    siftimages.append(img)

#feed to classifying neural network

#display performance data (time, memory, F1 score)
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))

#PATH 2
#run image dataset through Convolution Neural Network

#display performance data (time, memory, F1 score)
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))

#PATH 3
#run image dataset through Classifying Neural Network

#display performance data (time, memory, F1 score)
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred))