#!/usr/bin/python3
"""
QRCode file generator
"""
# standard library imports
import qrcode
import uuid


def qr_gen(data, box_size=10, border=4, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    type(img)  # qrcode.image.pil.PilImage
    filename = str(uuid.uuid4())
    img.save(f"./qr_ify/encoded_qrcode_img/{filename}.png")
    print(f"QRcode generated: {filename}.png")
    return
