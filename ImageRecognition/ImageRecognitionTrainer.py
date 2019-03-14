
from PIL import Image
from keras.datasets import cifar10
from matplotlib import pyplot as plt

from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.layers import Dense, Flatten, Dropout
from keras.optimizers import SGD
from keras.constraints import maxnorm

from keras.utils import np_utils

import h5py


cat_image_path = 'C:\\Users\\Shefaa\\Desktop\\PythonAI-BitDegree\\ImageRecognition\\cat.jpg'
cat_image = Image.open(cat_image_path)
#cat_image.show()


label = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']


# ==================== Dataset Loading and Preparation =========================

# loading the training and testing data as tuples (~80% for training and ~20% for testing)
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# Preparing the data to be in float32 type
new_X_train = X_train.astype('float32')
new_X_test = X_test.astype('float32')

# Normalizing the data to be in the range between 0 and 1
new_X_train /= 255
new_X_test /= 255

# Converting y values into categorical data
new_y_train = np_utils.to_categorical(y_train)
new_y_test = np_utils.to_categorical(y_test)


# =============== Example of Accessing An Instance in the Dataset =============

# Accessing a specific instance of the dataset
index = 5

# Returning the image as a 2D tuple of values between 0 and 1 (intensity value of the pixels)
display_image = X_train[index]

# Returning the label index of the accessed image
display_label = y_train[index][0]


# Rendering and showing the image using PyPlot
# We can use PIL library to do this as well
# plt.imshow(display_image)
# plt.show()
# print(label[display_label])


# ============================ NN Model Setup ===============================

# Creating NN Sequential model
model = Sequential()

# Adding layers to the NN sequential model
# Adding the 2D Convolution layer. Input_shape should be specified
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))

# Adding the 2D Max Pooling layer
model.add(MaxPooling2D(pool_size=(2, 2)))

# Adding Flatten layer
model.add(Flatten())

# Adding one Dense layer. 512 units because of 32*32 2D layer and divided by 2 because of the pool size.
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))

# Adding Dropout layer to reduce overfitting
model.add(Dropout(0.5))

# Adding one more Dense layer
model.add(Dense(10, activation='softmax'))


# Optimizing using SGD (Stochastic gradient descent) optimizer
optimizer = SGD(lr=0.01)

# Preparing the model for compiling and testing
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Fitting/Building the model
model.fit(new_X_train, new_y_train, batch_size=32, epochs=1)

# Saving the model in h5 file type
model.save('trained_model.h5')
