import pyqrcode

# لینک مورد نظر را در اینجا قرار دهید
link = "http://coffeeshoptest.onlinewebshop.net"

# نام فایل را در اینجا قرار دهید
file_name = "qrcode.png"

# ایجاد کد QR با استفاده از لینک
qr_code = pyqrcode.create(link)

# ذخیره کردن کد QR در فایل
qr_code.png(file_name + ".png", scale=8)
print("seccesfully ")
