import qrcode as qr
from PIL import Image

msg = input("Enter your message : ")
name = input("Enter your name of the file : ")
qr = qr.QRCode(version = 1, 
               error_correction  = qr.constants.ERROR_CORRECT_H,
               box_size = 10, border = 5,)
qr.add_data(msg)
qr.make(fit=True)
# Create an image from the QR code data
img = qr.make_image(fill_color = "black", back_color = "white")
img.save(f"{name}.png")
print("Your QR is generated...!")
end = input("Enter any key to exit.....")