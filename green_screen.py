import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


def nothing(x):
    pass


cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)

cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    boolean, frame = cap.read()

    # converting frame to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos("LH", "Tracking")
    lower_saturation = cv.getTrackbarPos("LS", "Tracking")
    lower_value = cv.getTrackbarPos("LV", "Tracking")

    upper_hue = cv.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv.getTrackbarPos("US", "Tracking")
    upper_value = cv.getTrackbarPos("UV", "Tracking")

    lower_bound = np.array([lower_hue, lower_saturation, lower_value])
    upper_bound = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv.inRange(hsv, lower_bound, upper_bound)

    output = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("Input", frame)
    cv.imshow("Stream", output)
    cv.imshow("Mask", mask)

    k = cv.waitKey(1) & 0xFF

    if k == 27:
        break

cv.release()
cv.destroyAllWindows()
