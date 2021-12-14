# ovdje definirajte dodatne datoteke ako su vam potrebne
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import time


# TODO: napisite funkciju koja oznacava 4 tocke na ulaznoj slici i spaja ih pravcima - za provjeru 4 tocke perspektivne transformacije
def plotArea(image, pts):

    return


# TODO: napisite funkciju za filtriranje po boji u HLS prostoru
# ulaz je slika u boji, funkcija vraca binarnu sliku te maske za bijelu, zutu boju i ukupnu masku
def filterByColor(image):
    # TODO: pretvorite sliku iz BGR u HLS
    img_hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #granice za zutu i bijelu
    # white_mask = cv2.inRange(img_hls, (0,160,0), (180,255,255))
    # yellow_mask = cv2.inRange(img_hls, (20,60,80), (30,255,255))

    lower = np.uint8([0,160,0])
    upper = np.uint8([180,255,255])
    white_mask = cv2.inRange(img_hls, lower, upper)

    lower = np.uint8([20,60,80])
    upper = np.uint8([30,255,255])
    yellow_mask = cv2.inRange(img_hls, lower, upper)

    mask = cv2.bitwise_or(white_mask, yellow_mask)  

    return mask


# TODO: napisite funkcija koja detektira dva maksimuma u sumi binarne slike po "vertikali"
# def getTwoPeaks(binary_img):
#     sums = np.ndarray.sum(binary_img, axis=-1)
#     sums = sums
#     x1 = np.argmax(sums)
    
#     xs = x1 - 50
#     xf = x1 + 50
#     if xs < 0:
#         xs == 0
#     if xf > len(sums):
#         xf = len(sums)

#     x2_val = 0
#     x2 = 0

#     for i in range(0, xs):
#         if i == x1:
#             continue
#         if sums[i] > x2_val:
#             x2_val = sums[i]
#             x2 = i

#     for i in range(xf, len(sums)):
#         if i == x1:
#             continue
#         if sums[i] > x2_val:
#             x2_val = sums[i]
#             x2 = i

#     if x1 < x2:
#         x_left = x1
#         x_right = x2
#     else:
#         x_left = x2
#         x_right = x1

#     print(x_left, x_right)
#     return x_left, x_right

def getTwoPeaks(binary_img):

    # sumiraj binarnu sliku po vertikali
    column_sums = np.sum(binary_img, axis=0) 
    columns_sums2 = column_sums.copy()

    # pronadji prvi maksimum
    x1 = np.argmax(column_sums)

    # postavi sve oko njega na nekoj udaljenosti na nulu
    x1_1 = x1 - 150
    x1_2 = x1 + 150

    if x1_1 < 0:
        x1_1 = 0
    if x1_2 > len(column_sums):
        x1_2 = len(column_sums)

    column_sums[x1_1:x1_2] = 0

    # pronadji drugi maksimum
    x2 = np.argmax(column_sums)
    
    if x1 > x2:
        x_left = x2
        x_right = x1
    else:
        x_left = x1
        x_right = x2

    return x_left, x_right


# TODO: prikazite voznu traku u ulaznoj slici; ako vozilo prelazi u drugu traku tada iskljucite prikaz i ispisite upozorenje
def showLane(original_img, x_left, x_right, y1, y2, M_inv):
    if x_left < 350 and x_right > 800:
        src_left = np.array([[x_left,y1],[x_left,y2]], dtype=np.float32)
        src_right = np.array([[x_right,y1],[x_right,y2]], dtype=np.float32)

        dst_left = cv2.perspectiveTransform(np.array([src_left]), M_inv)
        dst_right = cv2.perspectiveTransform(np.array([src_right]), M_inv)

        dst_left = dst_left[0,:,:]
        dst_right = dst_right[0,:,:]
        pts = np.append(dst_left, np.flip(dst_right, axis=0), axis=0)
        pts = pts.reshape((-1,1,2)).astype(np.int32)

        overlay = original_img.copy()
        cv2.fillPoly(overlay, [pts], color=(0, 255, 100))
        cv2.addWeighted(overlay, 0.35, original_img, 1 - 0.35, 0, original_img)

    else:
        cv2.putText(original_img, "Upozorenje!", (int(width/2)-140, 150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_4)

    return original_img
    

mainPath = os.path.join(os.getcwd(), "ferit")
pathResults = os.path.join(mainPath, "results")
pathVideos = os.path.join(mainPath, "videos")
videoName  = 'video2.mp4'

video = cv2.VideoCapture(os.path.join(pathVideos, videoName))

width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

k = 0
fps = 0



# src = np.array([(617, 446), (766, 449), (930, 559), (447, 563)])
# dst = np.array([(100, 800), (600, 800), (600, 100), (100, 100)])

src = np.array([
    [375, 626],
    [1043, 626],
    [792, 460],
    [607, 460]],
    dtype = np.float32)

dst = np.array([
    [320, 720],
    [960, 720],
    [960, 0],
    [320, 0]],
    dtype = np.float32)
src = np.float32(src[:, np.newaxis, :])
dst = np.float32(dst[:, np.newaxis, :])
M = cv2.getPerspectiveTransform(src, dst)
M_inv = cv2.getPerspectiveTransform(dst, src)



while(True):
    _, frame = video.read()
    if frame.any() != None:
        k += 1

    cv2.imshow("org", frame)


    # TODO: Pozovite funkciju za filtriranje po boji nad ulaznim okvirom
    frame_filtered = filterByColor(frame)

    # TODO: Transformirajte filtriranu binarnu sliku
    frame_transformed = cv2.warpPerspective(frame_filtered, M, (int(width), int(height)), flags=cv2.INTER_LINEAR)
    cv2.imshow("trans", frame_filtered)


    # TODO: Pozovite funkciju koja pronalazi dva maksimuma u "vertikalnoj sumi" transformirane binarne slike
    x1, x2 = getTwoPeaks(frame_transformed)
    print(x1, x2)
    # TODO: Pozovite funkciju koja oznacava voznu traku u originalnom video okviru; u slucaju prelaska u drugu ispisuje upozorenje 

    frame_final = showLane(frame, x1, x2, 0, frame_filtered.shape[0], M_inv)
    cv2.imshow("Final", frame_final)

    # TODO: Izracunajte vrijeme obrade u fps


    # TODO: Prikazite vrijeme obrade i redni broj okvira u gornjem lijevom cosku ulaznog video okvira


    # TODO: Prikazite okvir pomocu cv2.imshow(); i sve ostale medjurezultate kada ih napravite

    key =  cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break



# TODO: Unistite sve prozore i oslobodite objekt koji je kreiran pomocu cv2.VideoCapture
