from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from picamera import PiCamera
from time import sleep
import smtplib

count = 0

camera = PiCamera()

while True:
    print('What email would you like to send these pictures from?')
    print('Make sure that it supports outside applications mailing first...')
    from_mail = input()
    print('Is ', from_mail, ' the correct email? y/n')
    user = input()

    if user == 'y':
        break
    elif user == 'n':
        continue
    else:
        print("We're going to ask again, because you used an invalid response")

while True:
    print('What is the password for the sending email?')
    from_password = input()
    print('Is ', from_password, ' the correct password? y/n')
    user = input()

    if user == 'y':
        break
    elif user == 'n':
        continue
    else:
        print("We're going to ask again, because you used an invalid response")

while True:
    print('What email would you like to send these pictures to?')
    to_mail = input()
    print('Is ', to_mail, ' the correct email? y/n')
    user = input()

    if user == 'y':
        break
    elif user == 'n':
        continue
    else:
        print("We're going to ask again, because you used an invalid response")

while True:
    print('What would you like to label these pictures as? You cannot use the / symbol.')
    name = input()
    print('Is ', name, ' the correct label? y/n')
    user = input()

    if user == 'y':
        break
    elif user == 'n':
        continue
    else:
        print("We're going to ask again, because you used an invalid response")
  
msg = MIMEMultipart()

msg['From'] = from_mail
msg['To'] = to_mail
msg['Subject'] = "A picture for you"
body = "A picture for you."

print('How many pictures do you want to take?')
user = int(input())


while count < user:

    photo = '/home/pi/Pictures/' + name + str(count) + '.jpg'
    camera.start_preview()
    sleep(3)
    camera.capture(photo)
    camera.stop_preview()


    msg.attach(MIMEText(body, 'plain'))

    filename = name + str(count) + ".jpg"
    attachment = open(photo, "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(from_mail, from_password)
    text = msg.as_string()
    s.sendmail(from_mail, to_mail, text)
    s.quit()

    count += 1
    sleep(1)
