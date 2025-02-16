import cv2
import os
import numpy as np

img = cv2.imread("C:/users/deepanshika/OneDrive/Desktop/New_folder/picture.png")

img = img.astype(np.uint8)

msg = input("Enter secret message : ")
password = input("Enter a passcode : ")

d = {chr(i): i for i in range(256)}
m, n, z = 0, 0, 0

msg_length = len(msg)
img[n, m, z] = msg_length
n += 1

for char in msg:
    img[n, m, z] = d[char]
    n += 1
    if n >= img.shape[0]:
        m += 1
        n = 0
    z = (z+1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")