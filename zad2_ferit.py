import glob
import os
from PIL import Image, ImageOps

path = os.path.join(os.getcwd(), "ferit/images")
savePath = os.path.join(os.getcwd(), "ferit/output")
files = glob.glob(path + '/**/*.jpg', recursive=True)


images = []
for i in files:
    images.append(Image.open(os.path.join(path, i)))

for f in files:
    print(f)

for i in range(len(images)):
    ImageOps.grayscale(images[i]).save(os.path.join(savePath, "img"+str(i)+".jpg"))
