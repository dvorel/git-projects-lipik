
from PIL import Image
import os



image = Image.open(os.path.join(os.getcwd(), "ferit/vehicle.jpg"))
w, h = image.size
w90 = w*(h/w)
print("Rezolucija: ", h, w)
image_90 = image.rotate(-90)
image_90.show()
image_90.save(os.path.join(os.getcwd(), "ferit/vehicle_90.jpg"))

image_90 = image_90.crop(((w-w90)/2, 0, w90+((w-w90)/2), h))
image_90.save(os.path.join(os.getcwd(), "ferit/vehicle_90cropped.jpg"))
image_90.show()

newimg = Image.new("RGB", (int(w+w90), int(h)))
newimg.paste(image)
newimg.paste(image_90, (w, 0))
newimg.show()
newimg.save(os.path.join(os.getcwd(), "ferit/vehicle_90combined.jpg"))
