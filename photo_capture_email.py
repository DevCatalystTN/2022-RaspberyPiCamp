#Captures pictures and emails them to user
from email.mime.multipart import MIMEMultipart#import for email headings
from email.mime.text import MIMEText#import for email messages
from email.mime.base import MIMEBase#import for email attachments
from email import encoders#import to encrypt emailed files for handling
import smtplib#simple mail transfer protocol

from picamera import PiCamera#import camera
from time import sleep#import sleep for delay time

camera = PiCamera()#shortening camera syntax
from_mail = 'merpinkley@gmail.com'#setting the sender's email
to_mail = 'micah.pinkley@my.uu.edu'#setting the receiver's email
msg = MIMEMultipart()#defining the msg variable to hold the header values

camera.start_preview(alpha=192)
#starts a preview that allows you to still see the code running
    

photo = "/home/pi/image.jpg"#sets the filename for the captured photo
sleep(5)#delays the camera slightly 
camera.capture(photo)#captures a photo and saves it
          
msg['From'] = from_mail#sets the header 'from' value
msg['To'] = to_mail#sets the header 'to' value
msg['Subject'] = "SPi Cam 30 minute"# sets the header 'subject'
body = "SPi motion Cam picked this up."# initializes the email body
filename = photo#sets the file name for the email
msg.attach(MIMEText(body, 'plain'))#attaches the email message
attachment = open(photo, "rb")#attaches the file from it's path
p = MIMEBase('application', 'octet-stream')#sets file parameters
p.set_payload((attachment).read())#sets the file
encoders.encode_base64(p)#encodes the file
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#adds the header for the picture attachment

msg.attach(p)#finishes attaching the file

s = smtplib.SMTP('smtp.gmail.com', 587)#sets the mail protocol
s.starttls()#Starts an email session
s.login(from_mail, 'Pudding1')#logs into the sender email
text = msg.as_string()#uses the set parameters from msg
s.sendmail(from_mail, to_mail, text)#sends the email
s.quit()#ends the email session

camera.stop_preview()#ends preview if ever reached




