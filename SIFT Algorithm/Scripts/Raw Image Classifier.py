import cv2, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path =  os.path.join( os.path.abspath(os.path.join(dir_path, os.pardir)), "Dataset & Modified Datasets")
original_img_path = os.path.join( data_path, "leaf-classification\\images")
default_img_path = os.path.join( data_path, "leaf-classification-jpg-resized")
train = pd.read_csv(os.path.join( data_path, "leaf-classification\\mapping.csv"))
species = train.species.sort_values().unique()

def image_vector_generator(source = False):
    X = []
    Y = []
    speciesdict = {}
    numberofspecies = 0
    species = [1,2,3,4,5,6,7,8,9,10,11,12,13, 14, 15]
    for i in range(len(train)):
        if train.species[i] not in speciesdict:
            speciesdict[train.species[i]] = numberofspecies
            numberofspecies += 1
        if speciesdict[train.species[i]] in species:
            Y.append(speciesdict[train.species[i]])
            img = cv2.imread(os.path.join(original_img_path if source else default_img_path, str(train.id[i]) + ".jpg"))
            if source:
                img = cv2.resize(img, (300, 300),interpolation=cv2.INTER_NEAREST)
            img = np.array(img).flatten()
            X.append(img)
    return X, Y

def mlp_train_test_report():
    mlp = MLPClassifier(verbose=True, max_iter=600000)
    mlp.fit(X_train, Y_train)

    predicitions = mlp.predict(X_test)
    print(classification_report(Y_test, predicitions))

    fig, axes = plt.subplots(1, 1)
    axes.plot(mlp.loss_curve_, 'o-')
    axes.set_xlabel("number of iteration")
    axes.set_ylabel("loss")
    plt.show(block=True)


if __name__ == "__main__":
    input_source = input("Do you want to run the Raw Image Classifier with (default)SVG Resizing(1) or Interpolated Resizing(2), (Please enter 1/2):")
    if input_source == '2':
        print('you selected Interpolated Resizing')
    else:
        print('you selected SVG Based Resizing')
    print('This script may take > 5 minutes to execute, you will experience two prolonged periods with no terminal text activity, just be patient!')
    X, Y = image_vector_generator(input_source == '2')
    # Split the data into train/test sets
    split = int(len(X) *0.7)
    X_train, X_test = X[:split], X[split:]
    Y_train, Y_test = Y[:split], Y[split:]
    mlp_train_test_report()