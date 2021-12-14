# ovdje definirajte dodatne biblioteke ako su vam potrebne
import numpy as np
import cv2
import math
import os


# TODO: napisite funkciju za detekciju rubova; funkcija vraca binarnu sliku s detektiranim rubovima
def detectEdges(image):        
    canny_image = cv2.Canny(image, 100, 120)
    
    return canny_image


# TODO: napisite funkciju za filtriranje po boji u HLS prosotru
# ulaz je slika u boji, funkcija vraca binarnu sliku te maske za bijelu, zutu boju i ukupnu masku
def filterByColor(image):
    # TODO: pretvorite sliku iz BGR u HLS
    img_hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    #granice za zutu i bijelu
    white_mask = cv2.inRange(img_hls, (0,200,0), (180,255,255))
    yellow_mask = cv2.inRange(img_hls, (20,0,100), (30,255,255))

    mask = cv2.bitwise_or(white_mask, yellow_mask)    
    
    result = cv2.bitwise_and(img_hls, img_hls, mask=mask)    

    return result


# TODO: napisite funkciju za pronalazenje pravaca lijeve i desne kolnice oznake
# ulaz je binarna slika, a izlaz dvije liste koje sadrze pravce koji pripadaju lijevoj odnosnoj desnoj kolnickoj oznaci
def findLines(img, cimg):

    # TODO: koristite cv2.HoughLinesP() kako biste dobili linije na slici
    lines = cv2.HoughLinesP(img, 1, np.pi/180, 0, minLineLength=5)
    
    # od svih linija treba pronaci one koje predstavljaju lijevu odnosno desnu uzduznu kolnicku oznaku
    linesLeft = []
    linesRight = []
    
    # TODO: pokusajte razumjeti iduci kod; mozete li odgonetnuti cemu sluzi pojedini dio?
    try:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if abs(x2-x1) <= 1.0:   # ako je linija okomita
                b = np.inf
                a = np.inf
                x_val = x1
                lineAngle = 90.0
            else:
                a = (y2-y1)/(x2-x1)
                b = y1 - a*x1
                x_val = (img.shape[0] - b)/a
                lineAngle = math.atan2((y2-y1), (x2-x1)) * 180/np.pi
            
            if x_val > 150.0 and x_val < 1200.0:

                # lijeva i desna linija
                if lineAngle > 10.0 and  lineAngle <=90.0:
                    if x_val > 450.0 and x_val < 800.0:
                        linesRight.append([a,b,1,x_val])
                    else:
                        linesRight.append([a,b,0,x_val])
                elif lineAngle < -10.0 and lineAngle >= -90.0:
                    if x_val > 450.0 and x_val < 800.0:
                        linesLeft.append([a,b,1,x_val])
                    else:
                        linesLeft.append([a,b,0,x_val])
    except:
        linesRight = []
        linesLeft = []

    return linesRight, linesLeft


# TODO: dovrsite funkciju koja oznacava sa zelenom povrsinom voznu traku (podrucje unutar pravaca) te ispisuje upozorenje na originalni ulazni frame
def drawLane(linesLeft, linesRight, frameToDraw):

    ymin = 0
    ymax = frameToDraw.shape[0]

    if linesLeft and linesRight:
        

        if linesLeft[0][1] != np.inf and linesLeft[0][1] != np.inf:

            x1_1 = int((ymin - linesLeft[0][1]) / linesLeft[0][0])
            x1_2 = int((ymax - linesLeft[0][1]) / linesLeft[0][0])
        else:
            x1_1 = linesLeft[0][3]
            x1_2 = linesLeft[0][3]
        
        if linesRight[0][1] != np.inf and linesRight[0][1] != np.inf:    
            
            x2_1 = int((ymin - linesRight[0][1]) / linesRight[0][0])
            x2_2 = int((ymax - linesRight[0][1]) / linesRight[0][0])
        else:
            x2_1 = linesRight[0][3]
            x2_2 = linesRight[0][3]


        if linesLeft[0][2] == 0 and linesRight[0][2] == 0:
            contours = np.array([[x1_1,ymin+RoIymin], [x2_1,ymin+RoIymin], [x2_2, ymax+RoIymin], [x1_2,ymax+RoIymin]])
            overlay = frameToDraw.copy()

            cv2.fillPoly(overlay, [contours], color=(0, 255, 100))
            frameToDraw = cv2.addWeighted(frameToDraw, 0.7, overlay, 0.3, 0)
            # TODO: dodajte overlay pomocu funkcije cv2.addWeighted()

    
    if linesLeft:
        if linesLeft[0][2] == 1:
            # TODO: koristite funkcije cv2.putText kako biste na ekranu crvenim slovima ispisali upozorenje
            cv2.putText(frameToDraw, "Upozorenje!", (200,200), 2, 4, (0,0,255))
            print("Upozorenje")

    if linesRight:
        if linesRight[0][2] == 1:
            cv2.putText(frameToDraw, "Upozorenje!", (200,200), 2, 4, (0,0,255))
            print("Upozorenje")
        
    return frameToDraw



mainPath = os.path.join(os.getcwd(), "ferit")
pathResults = os.path.join(mainPath, "results")
pathVideos = os.path.join(mainPath, "videos")
videoName  = 'video2.mp4'

video = cv2.VideoCapture(os.path.join(pathVideos, videoName))

width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

#cv2.namedWindow("Line Detection", cv2.WINDOW_NORMAL)




# ovdje definirajte sve ostale varijable po potrebi koje su vam potrebne za razvoj rjesenja
k = 0
RoIymin = 460
RoIymax = 620

while True:

    # TODO: ucitaj frame pomocu metode read, povecaj k za jedan ako je uspjesno ucitan frame
    _, frame = video.read()
    if frame.any() != None:
        k += 1

    
    # TODO: kreiraj regiju od interesa (RoI) izdvajanjem dijela numpy polja koje predstavlja frame
    
    
    frame_roi = frame[int(12*(height/20)):int(17*(height/20)), :]
    cv2.imshow("Line Detection", frame_roi)

    # TODO: pozovite funkciju za filtriranje po boji

    cv2.imshow("Filtered", filterByColor(frame_roi)[0])
    frame_filtered = filterByColor(frame_roi)
    print(frame_filtered.shape[:2])

    # TODO: pozovite funkciju za detekciju rubova na filtriranoj slici kako bi ste smanjili kolicinu piksela koji se dalje procesiraju
    
    frame_canny = detectEdges(frame_filtered)
    cv2.imshow("canny", frame_canny)

    # TODO: pozovite funkciju za pronalazak pravaca lijeve i desne linije na slici s rubovima
    l1, l2 = findLines(frame_canny, frame_roi)
    print(l1, l2)

    # TODO: pozovite funkciju za prikaz vozne trake
    cv2.imshow("lanes", drawLane(l1, l2, frame))


    # TODO: prikazi frame pomocu cv2.imshow(); i sve ostale medjurezultate kada ih napravite

    #cv2.imshow()

    

    key =  cv2.waitKey(1) & 0xFF 
    if key == ord('q'):
        break
    
    # TODO: ovdje ispisite vrijeme procesiranja jednog okvira
    print("Vrijeme obrade u fps: ")


# TODO: ovdje unistite sve prozore i oslobodite objekt koji je kreiran pomocu cv2.VideoCapture
