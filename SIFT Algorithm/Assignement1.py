import os
import cv2
import Sift
import random

#load image dataset from input file
directory = "input\Dog"
X = []
Y = []
for filename in os.listdir(directory):
    # load the image file using opencv
    img = cv2.imread(os.path.join(directory, filename))
    # append the image to the list
    X.append(img)
    Y.append(1)
#load image dataset from input file
directory = "input\Cat"
for filename in os.listdir(directory):
    # load the image file using opencv
    img = cv2.imread(os.path.join(directory, filename))
    # append the image to the list
    X.append(img)
    Y.append(0)

# shuffle the data
data = list(zip(X, Y))
random.shuffle(data)
X, Y = zip(*data)

# split the data
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
Y_train, Y_test = Y[:split], Y[split:]

#PATH 1
#run the entire input dataset through sift feature extractor
X_train_sift = []
for img in X_train:
    X_train_sift.append(Sift.get_kp(img))

X_test_sift = []
for img in X_test:
    X_test_sift.append(Sift.get_kp(img))

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