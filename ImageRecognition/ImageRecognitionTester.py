from PIL import Image
import numpy as np
from keras.models import load_model


# Loading our pre-trained model
model = load_model('trained_model_epo10.h5')

# Preparing recognition labels
labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# Loading and resizing a testing image
pathname = input('Enter image pathname: ')
input_image = Image.open(pathname)
input_image = input_image.resize((32, 32), resample=Image.LANCZOS)

# Converting testing image into an array
image_array = np.array(input_image)
image_array = image_array.astype('float32')
image_array /= 255.0
image_array = image_array.reshape(1, 32, 32, 3)

# Predicting the answer
answer = model.predict(image_array)
print(labels[np.argmax(answer)])
