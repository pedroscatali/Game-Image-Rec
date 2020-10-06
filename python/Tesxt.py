import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Python383\Scripts'
img = cv.imread('Imgp.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(
    gray, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (18, 18))
dilation = cv.dilate(thresh1, rect_kernel, iterations=1)
# Finding contours
contours, hierarchy = cv.findContours(dilation, cv.RETR_EXTERNAL,
                                       cv.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]

    # Open the file in append mode
    file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    # Appending the text into file
    file.write(text)
    file.write("\n")

    # Close the file
    file.close
