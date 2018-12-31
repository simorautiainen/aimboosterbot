import cv2
import numpy as np
import pyautogui


image = "dot7.png"
img = cv2.imread(image)
height, width, channels = img.shape

def imagesearch(image):
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < 0.8:
        return [-1,-1]
    return max_loc

while True:
    pos = imagesearch(image)
    while pos[0] == -1:
        pos = imagesearch(image)
    pyautogui.moveTo(pos[0] + (width / 2), pos[1] + (height / 2))
    pyautogui.click()
