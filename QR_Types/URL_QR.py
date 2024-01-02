import qrcode

def generate_qr_code(url, file_name='qrcode.png'):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data (URL) to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

    print(f"QR code for {url} generated and saved as {file_name}")

if __name__ == "__main__":
    # Example usage:
    url_to_encode = input("Enter the URL to generate a QR code for: ")
    output_file_name = input("Enter the output file name (default is qrcode.png): ") or 'qrcode.png'
    
    generate_qr_code(url_to_encode, output_file_name)
