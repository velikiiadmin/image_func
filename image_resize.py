from PIL import Image, ImageFilter


image = str(input())
img = Image.open(image)

print(img.size)

img.thumbnail((400, 200))

img.save('thumbnail.jpg')