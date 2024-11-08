from random import randint

from PIL import Image, ImageFile


class AvatarIt:
    def __init__(self, path, width: int, height: int):
        self.img: ImageFile = Image.open(path)
        self._width = width
        self._height = height
        pass

    def generate(self, width: int = None, height: int = None) -> ImageFile.ImageFile:
        w, h = self.img.size
        width, height = width or self._width, height or self._height

        p1X = randint(0, w - width)
        p1Y = randint(0, h - height)

        return self.img.crop((p1X, p1Y, p1X + width, p1Y + height))


if __name__ == '__main__':

    pass
