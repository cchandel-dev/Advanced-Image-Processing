import cv2, os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# https://www.kaggle.com/code/pierre54/bag-of-words-model-with-sift-descriptors

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path =  os.path.join( os.path.abspath(os.path.join(dir_path, os.pardir)), "Dataset & Modified Datasets")
svg_img_path = os.path.join(data_path, "leaf-classification-jpg-resized")
org_img_path = os.path.join(data_path, "leaf-classification\\images")
train = pd.read_csv(os.path.join(data_path, "leaf-classification\\mapping.csv"))
species = train.species.sort_values().unique()

def sift_feature_generator(source = False):
    print('generating sift feautures')
    img_path = svg_img_path
    if source:
        img_path = org_img_path
    dico = []
    sift = cv2.SIFT_create()
    for leaf in train.id:
        print('Pre - kmeans: extracting from image {}'.format(leaf))
        img = cv2.imread(os.path.join(img_path, str(leaf) + ".jpg"))
        kp, des = sift.detectAndCompute(img, None)

        for d in des:
            dico.append(d)

    k = np.size(species) * 10

    batch_size = np.size(os.listdir(img_path)) * 3
    kmeans = MiniBatchKMeans(n_clusters=k, batch_size=batch_size, verbose=1).fit(dico)


    kmeans.verbose = False

    histo_list = []

    for leaf in train.id:
        print('Post - kmeans: extracting from image {}'.format(leaf))
        img = cv2.imread(os.path.join(img_path, str(leaf) + ".jpg"))
        kp, des = sift.detectAndCompute(img, None)

        histo = np.zeros(k)
        nkp = np.size(kp)

        for d in des:
            idx = kmeans.predict([d])
            histo[idx] += 1/nkp # Because we need normalized histograms, I prefered to add 1/nkp directly

        histo_list.append(histo)

    X = np.array(histo_list)
    Y = []

    # It's a way to convert species name into an integer
    for s in train.species:
        Y.append(np.min(np.nonzero(species == s)))

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
    input_source = input("Do you want to run the Sift Classifier with (default)SVG Resizing(1) or Interpolated Resizing(2), (Please enter 1/2):")
    if input_source == '2':
        print('you selected Interpolated Resizing')
    else:
        print('you selected SVG Based Resizing')
    print('This script may take > 5 minutes to execute!')
    X, Y = sift_feature_generator(input_source == '2')
    # Split the data into train/test sets
    split = int(len(X) *0.7)
    X_train, X_test = X[:split], X[split:]
    Y_train, Y_test = Y[:split], Y[split:]
    mlp_train_test_report()