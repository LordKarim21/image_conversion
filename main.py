import os
from PIL import Image

DIRECTORY = r'Test'
FROM_EXTENSION = '.jpg'
TO_EXTENSION = '.png'
MAX_SIZE = (1024, 1024)


def walk(directiry):
    for root, dirs, files in os.walk(directiry):
        for name in files:
            conversion(os.path.join(root, name))


def conversion(file):
    resize(file)
    name, extension = os.path.splitext(file)
    if extension == FROM_EXTENSION:
        im = Image.open(file)
        im.save(name + TO_EXTENSION)
        os.remove(file)


def resize(file):
    im = Image.open(file)
    im.thumbnail(MAX_SIZE)
    im.save(file)


if __name__ == '__main__':
    walk(DIRECTORY)
