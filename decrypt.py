import cv2

image = cv2.imread("encryptedImage.png")

passcode = input("Enter the passcode for decryption : ")

if passcode == "1234":
    message = ""
    c = {i: chr(i) for i in range(256)}

    m, n, z = 0, 0, 0

    msg_length = image[n, m, z]
    n += 1

    for i in range(msg_length):
        char_value = image[n, m, z]
        message = message + c[char_value]
        n += 1
        if n >= image.shape[0]:
            m += 1
            n = 0
        z = (z+1) % 3

    print("Decrypt message : ", message)
else:
    print("You are not author")
