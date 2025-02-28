import cv2
import os

# Place the image in the working directory
image_path = "Photo.jpg"  
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not load the image. Check the file path.")
    exit()

# Get the image dimensions
height, width, _ = img.shape

# Secret message input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Mapping characters to ASCII values
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Encoding message into the image
n, m = 0, 0  # Row, Column positions

for i in range(len(msg)):
    # If message exceeds image size
    if n >= height:  
        print("Error: Message is too long for this image!")
        exit()
    
    img[n, m, 0] = d[msg[i]]  # Store ASCII in the Blue channel
    m += 1
    if m >= width:  # Move to next row if column limit exceeds
        m = 0
        n += 1

# Save and open the encoded image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens the image (Windows)

# Decryption process
message = ""
n, m = 0, 0

pas = input("Enter passcode for decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, 0]]
        m += 1
        if m >= width:
            m = 0
            n += 1
    print("Decrypted message:", message)
else:
    print("Access Denied: Incorrect passcode!")
