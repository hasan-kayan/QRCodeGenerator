# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  

# String which represents the QR code
embeddedURL = input("Please enter the url you want to embedded : ")
  
# Generate QR code
url = pyqrcode.create(embeddedURL)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)