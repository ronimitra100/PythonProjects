from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# Check out properties of the image 'img'
print(img)
print(img.format)
print(img.size)
print(img.mode)

# Check out methods supported by image 'img'
print(dir(img.mode))

filtered_img_1 = img.filter(ImageFilter.BLUR)
box = (100, 100, 400, 400)
region = filtered_img_1.crop(box)
region.save("cropped_and_blurred_pikachu.png", "png")

filtered_img_2 = img.filter(ImageFilter.SMOOTH)
resize = filtered_img_2.resize((300, 300))
resize.save("smooth_and_resized_pikachu.png", "png")

filtered_img_3 = img.filter(ImageFilter.SHARPEN)
crooked = filtered_img_3.rotate(90)
crooked.save("crooked_and_sharp_pikachu.png", "png")

# Convert to Grayscale image and show the image
filtered_img_4 = img.convert('L')
filtered_img_4.save("grey_pikachu.png", "png")
filtered_img_4.show()

img = Image.open('./astro.jpg')
print(img.size)

new_img1 = img.resize((400, 400))
# Doesn't keep aspect ration, i.e., squishes images if width/height ratio of original and final images don't match
new_img1.save('squished_thumbnail.jpg')

# Keeps the aspect ratio
img.thumbnail((400, 200))
img.save('thumbnail_with_aspect.jpg')
print(img.size)
