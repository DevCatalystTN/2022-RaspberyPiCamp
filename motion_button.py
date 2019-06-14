#Captures pictures using a button as the trigger
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from picamera import PiCamera
from gpiozero import Button
from time import sleep
import smtplib
import pygame.mixer
from pygame.mixer import Sound

pygame.init()

boolean = True
camera = PiCamera()
button = Button(4)
doorbell = pygame.mixer.Sound('/home/pi/doorbell-1.wav')
from_mail = 'sender email'
to_mail = 'receiving email'
msg = MIMEMultipart()

while boolean == True:
    if button.is_pressed:
        doorbell.play()
        sleep(.5)

        camera.start_preview(alpha=192)
        sleep(3)
        camera.capture("/home/pi/doorbell.jpg")
        camera.stop_preview()
        
        msg['From'] = from_mail
        msg['To'] = to_mail
        msg['Subject'] = "Doorbell Alert"
        body = "Someone's at the door!"
  
        msg.attach(MIMEText(body, 'plain'))
        filename = "doorbell.jpg"
        attachment = open("/home/pi/doorbell.jpg", "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(from_mail, 'Password')
        text = msg.as_string()
        s.sendmail(from_mail, to_mail, text)
        s.quit()
        
        boolean = False




