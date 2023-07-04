import qrcode

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qrcode.png")

# Example usage
url = "https://github.com/ArjunPraja"
generate_qr_code(url)
print("QR code generated successfully.")
