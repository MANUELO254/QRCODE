import cv2
import qrcode

# Generate QR code
qr_data = "https://www.pavicon.co.ke/"
myqr = qrcode.make(qr_data)
myqr.save("myqr.png", scale=8)

# Decode QR code using OpenCV
image = cv2.imread("myqr.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
qr_code_detector = cv2.QRCodeDetector()
decoded_info, points, straight_qrcode = qr_code_detector.detectAndDecode(gray)

if decoded_info:
    print(decoded_info)
else:
    print("No QR code detected.")
