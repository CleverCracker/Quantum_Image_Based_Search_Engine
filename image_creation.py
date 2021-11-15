from PIL import Image

# width = 3
# height = 3

# for i in range(width):
#     for j in range(height):
#         img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
#         img.putpixel((i, j), (0, 0, 0))
#         img.save('images/3x3/'+str(i)+str(j)+".jpg")
            
width = 4
height = 4

for i in range(width):
    for j in range(height):
        img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
        img.putpixel((i, j), (0, 0, 0))
        img.save('images/4x4/'+str(i)+str(j)+".jpg")
            