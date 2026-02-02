# QR-Code neu generieren:
# 1) URL unten ändern
# 2) python3 make_qr.py
import qrcode

URL = "https://example.com/konstanz-driver"  # <- HIER echte URL einsetzen (z.B. GitHub Pages / Netlify)

qr = qrcode.QRCode(border=2, box_size=10)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
print("Fertig: qr.png ->", URL)
