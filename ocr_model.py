import pytesseract
import cv2
import re

def extract_text(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    text = pytesseract.image_to_string(thresh)
    return text

def extract_values(text):
    hba1c = None
    glucose = None

    hba1c_match = re.search(r'Hb.?A.?[1l].*?([0-9]+\.[0-9])', text, re.IGNORECASE)
    glucose_match = re.search(r'Glucose.*?([0-9]+)', text, re.IGNORECASE)

    if hba1c_match:
        hba1c = float(hba1c_match.group(1))

    if glucose_match:
        glucose = float(glucose_match.group(1))

    return hba1c, glucose