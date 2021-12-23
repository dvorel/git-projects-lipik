import os
import cv2
import numpy as np
from skimage.feature import hog
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, r2_score

#global var-s
mean_width = 101
mean_height = 204

#funcs
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images
 
def resize_imgs(images):
    ret = list()
    for img in images:
        img = cv2.resize(img, (mean_width, mean_height))
        ret.append(img)
    return ret

def images_to_hog(images, show=False):
    hog_imgs = list()
    hog_desc = list()
    for img in images:
        desc, temp = hog(img, visualize=True)
        hog_imgs.append(temp)
        hog_desc.append(desc)

    if show:
        cv2.imshow("HOG0", hog_imgs[0])
    hog_desc = np.array(hog_desc)
    return hog_desc

def cut_img(img):
    x, y = img.shape[0:2]
    imgs = list()
    for i in range(0, x-mean_width-1, 10):
        for j in range(0, y-mean_height-1, 10):
            temp = img[j:j+mean_height, i:i+mean_width]
            temp = cv2.resize(temp, (mean_width, mean_height))
            imgs.append(temp)

    return imgs

def hog_reshape(desc):
    ret = list()
    for d in desc:
        t = d.reshape((1, -1))
        ret.append(t)
    return ret

#-----main-----
#load images from dirs
ped_dir = os.path.join(os.getcwd(), "data/dataset/ped")
no_ped_dir = os.path.join(os.getcwd(), "data/dataset/no_ped")
no_ped = load_images_from_folder(no_ped_dir)
ped = load_images_from_folder(ped_dir)
#resize
ped = resize_imgs(ped)
no_ped = resize_imgs(no_ped)
# #img->hog
ped_hog = images_to_hog(ped)
no_ped_hog = images_to_hog(no_ped)

# #labels
pedestrian_labels = np.ones((ped_hog.shape[0]))
no_pedestrian_labels = np.zeros((no_ped_hog.shape[0]))
# #combine
X = np.concatenate((ped_hog, no_ped_hog))
y= np.concatenate((pedestrian_labels, no_pedestrian_labels))
# #split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)
#train
model = MLPClassifier(random_state=1)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)

img_dir = os.path.join(os.getcwd(), "data/dataset/test_img.png")
test_img = cv2.imread(img_dir, cv2.IMREAD_GRAYSCALE)
test_cut = cut_img(test_img)
test_hog = images_to_hog(test_cut)
prob_list = np.array([])

for img in test_hog:
    p = model.predict_proba(img)
    prob_list.append(p)
#print(prob_list)



# print(score)
print("end")
