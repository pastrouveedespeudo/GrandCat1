from PIL import Image

def resize(image, save):
    im = Image.open(image)

    im = im.resize((50,50))

    im.save(save)

resize("image1.jpg", "image1.resize.jpg")
