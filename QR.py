
import pyqrcode
from pyqrcode import QRCode

a = "https://www.linkedin.com/in/jaspreet-nahal/"
url = pyqrcode.create(a)
url.svg("myqr.svg", scale=8)
url.png('myqr.png', scale=6)
