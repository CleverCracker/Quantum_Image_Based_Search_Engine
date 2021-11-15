import numpy as np
from PIL import Image


def image_normalization(imagePath, w=32, h=32):
    image = Image.open(imagePath).convert('LA').resize((w, h), Image.ANTIALIAS)
    image = np.array([[image.getpixel((x, y))[0]
                       for x in range(w)] for y in range(h)])

    # 2-dimentional data convert to 1-dimentional array
    image = image.flatten()
    # change type
    image = image.astype('float64')
    # Normalization(0~pi/2)
    image /= 255.0
    generated_image = np.arcsin(image)

    return generated_image
