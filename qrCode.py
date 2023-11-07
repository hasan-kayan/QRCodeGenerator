# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

# vCard information
vcard_info = """BEGIN:VCARD
VERSION:3.0
N:Erol;Eda
FN:Eda Erol
ORG:Poliark Inc
TITLE:Founder & CEO
TEL;TYPE=WORK,VOICE:+905397728894
EMAIL;TYPE=PREF,INTERNET:edaerol@poliark.com
URL:www.poliark.com
ADR;TYPE=WORK:;;USA | TR
END:VCARD"""

# Generate QR code
qr_code = pyqrcode.create(vcard_info)

# Create and save the svg file naming "myqr.svg"
qr_code.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
qr_code.png('myqr.png', scale = 6)
