import os
import qrcode
import pathlib
from qrcode.image.pure import PyPNGImage
import cv2
import json


def make_code(data) -> PyPNGImage:
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L,
    box_size=20,
    border=1,
)
    qr.add_data(data)
    qr.make()
    return qr.make_image()


def main():
    data = {
        'test': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        'one': 1,
        'two': 2,
        'three': 3
    }
    path = pathlib.Path('./qrcode.png')
    if path.exists():
        os.remove('./qrcode.png')

    qr = make_code(json.dumps(data))
    qr.save("qrcode.png")
    
    detector = cv2.QRCodeDetector()
    qrcode_image = cv2.imread('./qrcode.png')
    decoded, _, _ = detector.detectAndDecode(qrcode_image)
    
    print(json.loads(decoded))


if __name__ == "__main__":
    main()
