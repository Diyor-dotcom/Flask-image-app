from tensorflow import keras
import cv2
import numpy as np
model = keras.models.load_model('model_cifar10.h5')

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (32,32))
    img = img.astype('float32') / 255

    result = model.predict(np.expand_dims(img, axis=0))

    mapping = {
        0:'airplane',
        1:'automobile',
        2:'bird',
        3:'cat',
        4:'deer',
        5:'dog',
        6:'frog',
        7:'horse',
        8:'ship',
        9:'truck'
    }

    result_class = np.argmax(result, axis=1)[0]
    return mapping[result_class]



