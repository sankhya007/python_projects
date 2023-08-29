import qrcode
from PIL import Image
import tkinter as tk
from tkinter import PhotoImage

def generate_qr_and_display(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save("qr_code.png")
    
    root = tk.Tk()
    root.title("QR Code")
    img = PhotoImage(file="qr_code.png")
    label = tk.Label(root, image=img)
    label.pack()
    root.mainloop()

def main():
    link = input("Enter the link for which you want to generate a QR code: ")
    generate_qr_and_display(link)

if __name__ == "__main__":
    main()
