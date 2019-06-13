from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from picamera import PiCamera
from time import sleep
import smtplib

camera = PiCamera()
from_mail = 'merpinkley@gmail.com'
to_mail = 'micah.pinkley@my.uu.edu'
msg = MIMEMultipart()

msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = "S-Pi Cam Alert"
body = "The S-Pi Cam picked this up."


camera.start_preview()
sleep(10)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()


msg.attach(MIMEText(body, 'plain'))

filename = "image.jpg"
attachment = open("/home/pi/Desktop/image.jpg", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(from_mail, 'Pudding1')
text = msg.as_string()
s.sendmail(from_mail, to_mail, text)
s.quit()
