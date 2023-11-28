import qrcode
import webbrowser

def generate_qr_code(url, output_file):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_file)

if __name__ == "__main__":
    # Output file names
    qr_code_file = "qr_code.png"

    # URL for redirection
    redirect_url = "http://54.165.240.5"

    # Generate QR code
    generate_qr_code(redirect_url, qr_code_file)

    print(f"QR code generated. Open '{qr_code_file}' to view the link.")
