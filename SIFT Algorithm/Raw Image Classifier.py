import cv2, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

img_path = os.path.join( os.path.dirname(__file__), "leaf-classification-jpg-resized")
train = pd.read_csv(os.path.join( os.path.dirname(__file__), "leaf-classification\\mapping.csv"))
species = train.species.sort_values().unique()


def image_vector_generator():
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
            img = cv2.imread(os.path.join(img_path, str(train.id[i]) + ".jpg"))
            # img = cv2.resize(img, (300, 300),interpolation=cv2.INTER_NEAREST)
            img = np.array(img).flatten()
            X.append(img)
    return X, Y

def mlp_train_test_report():
    mlp = MLPClassifier(verbose=True, max_iter=600000)
    mlp.fit(X_train, Y_train)

    fig, axes = plt.subplots(1, 1)
    axes.plot(mlp.loss_curve_, 'o-')
    axes.set_xlabel("number of iteration")
    axes.set_ylabel("loss")
    plt.show(block=True)

    predicitions = mlp.predict(X_test)
    print(classification_report(Y_test, predicitions))


if __name__ == "__main__":
    X, Y = image_vector_generator()
    # Split the data into train/test sets
    split = int(len(X) *0.7)
    X_train, X_test = X[:split], X[split:]
    Y_train, Y_test = Y[:split], Y[split:]
    mlp_train_test_report()