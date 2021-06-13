import cv2

# Tytuł filmu = Stream live Video from Mobile Phone Camera with Python and Open CV
# adres z dodatkiem video pod jakim streaming servera w aplikacji ip camera na komórce się odbywa
capture = cv2.VideoCapture("http://192.168.0.228:8080/video")

while(True):
    # first variable represents we are not planing to use it - "_"
    _, frame = capture.read()
    #Pokaż obraz czarnobiały do poźniejsze obróbki
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('livestream', gray)

    mirror = cv2.flip(frame, 1)

    cv2.imshow('livestream', mirror)
    # q jako przycisk break
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()