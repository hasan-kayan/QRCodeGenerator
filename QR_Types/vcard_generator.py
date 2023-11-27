# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode



def vcard_QR(Name, Surname, Organization, Title, TEL, Email, URL, ADR):
    # vCard information
    vcard_info = """BEGIN:VCARD
    VERSION:3.0
    N:{};{}
    FN:{} {}
    ORG:{}
    TITLE:{}
    TEL;TYPE=WORK,VOICE:{}
    EMAIL;TYPE=PREF,INTERNET:{}
    URL:{}
    ADR;TYPE=WORK:{}
    END:VCARD""".format(Surname, Name, Name, Surname, Organization, Title, TEL, Email, URL, ADR)

    # Generate QR code
    qr_code = pyqrcode.create(vcard_info)

    # Create and save the svg file naming "myqr.svg"
    qr_code.svg("myqr.svg", scale = 8)

    # Create and save the png file naming "myqr.png"
    qr_code.png('myqr.png', scale = 6)
    
    return qr_code