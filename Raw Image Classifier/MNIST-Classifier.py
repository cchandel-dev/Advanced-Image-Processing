import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
# acquire MNIST data
from tensorflow.keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# reshape data for an MLP input
import numpy as np

train_images = np.reshape(train_images, (-1, 784))
test_images = np.reshape(test_images, (-1, 784))

# normalize data
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# convert labels to a one-hot vector
from tensorflow.keras.utils import to_categorical

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
# define network architecture
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer
from tensorflow.keras.layers import Dense

# #estimator will be decided below
mlp = MLPClassifier(early_stopping=False, warm_start=True)#, verbose=True, solver='adam', early_stopping=True)
#the parameters which will be modulated (and modulated values) are described below
parameter_space = {
    'hidden_layer_sizes': [(5, 25, 50,25, 5)],
    'activation':['logistic', 'relu',],
    'alpha': [ 0.00005, 0.0001],
    #'beta_1': [0.5, 0.7],
    #'beta_2': [0.9, 0.95],
}
#assign estimator, parameters to modulate, parallel jobs & cross validation to a GridSearchCV method
model = GridSearchCV(mlp, parameter_space, n_jobs=3, cv=3)

# #fit the model to the trainng set
history = model.fit(train_images, train_labels)
hist = mlp.fit()
# # train (fit)
# history = MLP.fit(train_images, train_labels, validation_data=(test_images, test_labels), epochs=50, batch_size=128)

# # evaluate performance
# test_loss, test_acc = MLP.evaluate(test_images, test_labels,
#                                    batch_size=128,
#                                    verbose=0)
# print("Test loss:", test_loss)
# print("Test accuracy:", test_acc)
label_prediction = model.predict(test_images)
print(classification_report(test_labels, label_prediction))


#print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))
# plot loss during training
plt.subplot(211)
plt.title('Loss')
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='test')
plt.legend()
# plot accuracy during training
plt.subplot(212)
plt.title('Accuracy')
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='test')
plt.legend()
plt.show()