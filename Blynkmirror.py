#define BLYNK_TEMPLATE_ID "TMPLej6CJLam"
#define BLYNK_DEVICE_NAME "raspberrypi Template"

import tweepy
import BlynkLib
import time
from sense_hat import SenseHat
import picamera
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import storeFileFB
from picamera import PiCamera
import os
from twilio.rest import Client
from dotenv import dotenv_values
from dotenv import load_dotenv
import cups
from escpos.connections import getNetworkPrinter
import BlynkLib
from datetime import datetime
import os, time
import subprocess
from PIL import Image


BLYNK_AUTH = 'j0CzYYYPriSRoxmRclMd0FX5Ge76woqy'

config = dotenv_values(".env")
load_dotenv()
sense = SenseHat()
sense.clear()
frame = 1
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Send an email with an attachment using SMTP
def send_mail(eFrom, to, subject, text, attachment):
    # SMTP Server details: update to your credentials or use class server
    smtpServer='smtp.gmail.com' 
    smtpUser='witmaster2021@gmail.com' 
    smtpPassword='ofhp aqmc cjws etcl' 
    port=587
    # open attachment and read in as MIME image
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msgImage['Content-Disposition'] = 'attachment; filename="image.jpg"'
    msg.attach(msgImage)
    msg['Subject'] = subject
    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.ehlo()
    s.starttls()
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()

# initialize Blynk
#Using Tweepy library I have obtained keys and tokens needed to gain access
@blynk.on("V3")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    twitter_auth_keys = {
         "consumer_key"        : "OpnwTUEbBonriWfRRWnxUk535",
         "consumer_secret"     : "cCVHWsblt1a3BWIMr8SCSu8ln8p3xuXkkJPL63AXZK3g3xtGLw",
         "access_token"        : "748636211359657988-yYt3xYLBTfHJw8uMen8A8odE6UC1oSt",
         "access_token_secret" : "bg3eJEdxBqPYdesFyA4Da9EzBgvruM7KYLqU4mV21qaTT"
        }
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
    #When button is equal to 1 a photo will be taken and sent to twitter
    if buttonValue=="1":
         print("About to take pic")
         with picamera.PiCamera() as camera:
             #Option to write a tweet with photo taken
             tweet = input("Enter Tweet :")
             camera.resolution = (1280, 720)
             camera.capture("/home/pi/MarvelMirror/images/image1.jpeg")
             print("Picture taken")
             filename = "/home/pi/MarvelMirror/images/image1.jpeg"
             # Upload image
             media = api.media_upload(filename)
             #camera gets closed here to allow for other buttons to take photos and use stream
             camera.close()
             api.update_status(status=tweet, media_ids=[media.media_id])


# This button is the photobooth button this sends a captured photo to a printer to be printed out over a wifi connection.
@blynk.on("V11")
def v11_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    FILE_PATH = "/home/pi/img_%s.%s"
    print("Button pressed!")
    datetime_string = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = FILE_PATH % (datetime_string, "jpg")
    os.system("raspistill -o %s" % filename)
    
    # convert
    image1 = Image.open(filename)
    im1 = image1.convert('RGB')
    jpg_filename = FILE_PATH % (datetime_string, "jpg")
    im1.save(jpg_filename)
 
    #sends to my HP printer and prints captured image.
    subprocess.run(["lp", "-d", "HP_ENVY_6000_series",jpg_filename ])



# register handler for virtual pin V0 Love Heart [Lights Button]
@blynk.on("V0")
def v0_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        #Here I have worked out individual coordinates and have used pink and blue to colour them
        sense.clear()
        #loveHeart shape
        sense.set_pixel(1,3,255,20,147)
        sense.set_pixel(1,4,255,20,147)
        sense.set_pixel(2,5,255,20,147)
        sense.set_pixel(4,6,255,20,147)
        sense.set_pixel(7,4,255,20,147)
        sense.set_pixel(6,2,255,20,147)
        sense.set_pixel(5,6,255,20,147)
        sense.set_pixel(3,6,255,20,147)
        sense.set_pixel(6,5,255,20,147)
        sense.set_pixel(7,3,255,20,147)
        sense.set_pixel(6,3,255,20,147)
        sense.set_pixel(5,3,255,20,147)
        sense.set_pixel(3,3,255,20,147)
        sense.set_pixel(2,3,255,20,147)
        sense.set_pixel(6,4,255,20,147)
        sense.set_pixel(5,4,255,20,147)
        sense.set_pixel(4,4,255,20,147)
        sense.set_pixel(3,4,255,20,147)
        sense.set_pixel(2,4,255,20,147)
        sense.set_pixel(4,5,255,20,147)
        sense.set_pixel(5,5,255,20,147)
        sense.set_pixel(3,5,255,20,147)
        sense.set_pixel(3,2,255,20,147)
        sense.set_pixel(5,2,255,20,147)
        sense.set_pixel(4,3,255,20,147)
        sense.set_pixel(2,2,255,20,147)
        sense.set_pixel(4,7,255,20,147)
        #blue background
        sense.set_pixel(4,2,0,0,255)
        sense.set_pixel(1,2,0,0,255)
        sense.set_pixel(0,2,0,0,255)
        sense.set_pixel(7,2,0,0,255)
        sense.set_pixel(7,1,0,0,255)
        sense.set_pixel(6,1,0,0,255)
        sense.set_pixel(5,1,0,0,255)
        sense.set_pixel(4,1,0,0,255)
        sense.set_pixel(3,1,0,0,255)
        sense.set_pixel(2,1,0,0,255)
        sense.set_pixel(1,1,0,0,255)
        sense.set_pixel(0,1,0,0,255)
        sense.set_pixel(7,0,0,0,255)
        sense.set_pixel(6,0,0,0,255)
        sense.set_pixel(5,0,0,0,255)
        sense.set_pixel(4,0,0,0,255)
        sense.set_pixel(3,0,0,0,255)
        sense.set_pixel(2,0,0,0,255)
        sense.set_pixel(1,0,0,0,255)
        sense.set_pixel(0,0,0,0,255)
        sense.set_pixel(7,7,0,0,255)
        sense.set_pixel(6,7,0,0,255)
        sense.set_pixel(5,7,0,0,255)
        sense.set_pixel(3,7,0,0,255)
        sense.set_pixel(2,7,0,0,255)
        sense.set_pixel(1,7,0,0,255)
        sense.set_pixel(0,7,0,0,255)
        sense.set_pixel(7,6,0,0,255)
        sense.set_pixel(6,6,0,0,255)
        sense.set_pixel(2,6,0,0,255)
        sense.set_pixel(1,6,0,0,255)
        sense.set_pixel(0,6,0,0,255)
        sense.set_pixel(0,5,0,0,255)
        sense.set_pixel(1,5,0,0,255)
        sense.set_pixel(7,5,0,0,255)
        sense.set_pixel(0,3,0,0,255)
        sense.set_pixel(0,4,0,0,255)
     
    else:
        sense.clear()


# register handler for virtual pin V6 [Photo Button]take photos and upload to firebase
@blynk.on("V6")
def v6_write_handler(value):
    # Global allows us to capture images globally opposed to local.
    global frame
    buttonValue = value[0]
    
    print(f'Current button value: {buttonValue}')
    camera = PiCamera()
    camera.start_preview()
     
    if buttonValue == "1":
        fileLoc = f'/home/pi/MarvelMirror/images/image{frame}.jpg'  # set location of image file and current time
        currentTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        camera.capture(fileLoc)  # capture image and store in fileLoc
        print(f'image {frame} taken at {currentTime}')  # print frame number to console
        storeFileFB.store_file(fileLoc)
        storeFileFB.push_db(fileLoc, currentTime)
        frame += 1
    camera.close()   

    
 # register handler for virtual pin V5 [Email Button] sends email with image attached with camera annotation.
@blynk.on("V5")
def v5_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
       # Send an email with an attachment using SMTP
       print("About to take pic")
       with picamera.PiCamera() as camera:
          camera.resolution = (1280,720)
          camera.annotate_text = 'YOU HAVE BEEN SNAPPED!'
          camera.capture("/home/pi/MarvelMirror/images/image1.jpeg")
          print("Picture taken")
          # so camera can close and other buttons function
          camera.close()
    now = datetime.now()
    currentTimes = now.strftime("%H:%M:%S")
    text = f'Hi we just snapped you,\n the attached image was taken today at {currentTimes}'
    send_mail('witmaster2021@gmail.com', 'sophiamcgee90@gmail.com', 'Snap You',text, "/home/pi/MarvelMirror/images/image1.jpeg") 


# register handler for virtual pin V4 [Temp Button] 
@blynk.on("V4")
def v4_write_handler(value):
    buttonValue=value[0]
    sense = SenseHat()
    sense.clear()    
    temp = sense.get_temperature() 
    
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        
        if temp >=23:
            sense.show_message("Temp is %.1f C" % temp, scroll_speed=0.10, text_colour=[0, 0, 255])
        else:
            sense.show_message("Too Cold to Register Reading It s Below 23 C", text_colour = [255, 0, 255])
            print(temp)

# register handler for virtual pin V2 [Quote Button] 
@blynk.on("V2")
def v2_write_handler(value):
     buttonValue=value[0]
     sense = SenseHat()
     sense.clear() 
     #assigning names to environment functions    
     temp = sense.get_temperature() 
     humidity = sense.get_humidity() 
     pressure = sense.get_pressure()
    
     print(f'Current button value: {buttonValue}')
     if buttonValue=="1":
        #list of if statements depending on temp,humidity and pressure in the room this is the quote button.
         if temp >=20:
             sense.show_message("Love the Outfit" , scroll_speed=0.05, text_colour=[0, 0, 255])
         if humidity >=20:
             sense.show_message("Your looking like a Babe", scroll_speed=0.05, text_colour=[0, 255, 0])
         if pressure >=20:
             sense.show_message("You are a 20 out of 10", scroll_speed=0.10, text_colour=[255, 0, 0])
         else:
            sense.show_message("Did you get dressed in the Dark", text_colour = [0, 0, 255])
            print(temp)
     
# register handler for virtual pin V2 [Motion Detect Button] 
@blynk.on("V8")
def v8_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}') 
    if buttonValue=="1":
        account_sid = os.getenv('account_sid')
     # Your Auth Token from twilio.com/console
        auth_token  = os.getenv('auth_token')
        client = Client(account_sid, auth_token)
        #not a hundred percent sure if my motion logic is correct on this one but this sends a SMS message if motion is detected.
        i = 0
        while True:
            if i != 0:
                a = x
                b = y
                c = z
            motion = sense.get_accelerometer_raw()    
            x = motion['x']
            y = motion['y']
            z = motion['z']
            x = round(x, 0)
            y = round(y, 0)
            z = round(z, 0)
            if i != 0:
                if x != a:
                    print('motion detected')
                    break
                if y != b:
                    print('motion detected')
                    break
                if x != c:
                    print('motion detected')
                    break
            else:
                i += 1
        #messages from preregistered number from twilio and sends the body message to my phone
        message = client.messages.create(
            to="+353838760848", 
            from_="+19592650883",
            body="Welcome to Marvel Mirror.We at Marvel Mirror would like to thank you for trying out our Product If you would like to check out our Website just click the link below.Otherwise Have a lovely day..."  "https://marvelmirror1.glitch.me")
            
            
    #tmr_start_time = time.time()
 # infinite loop that waits for event
while True:
    blynk.run()
    blynk.virtual_write(1, round(sense.temperature,2))
    time.sleep(1)
    