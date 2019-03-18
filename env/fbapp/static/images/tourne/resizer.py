from PIL import Image

def resize(image, save):
    im = Image.open(image)

    im = im.resize((211,239))

    im.save(save)

resize("two.jpg", "two.jpg")
