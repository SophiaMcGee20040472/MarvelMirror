Student Name:Sophia McGee

Student No: 20040472
 
Readme 

I have created a Blynk application using Datastream virtual pins to trigger events,
I have programmed this using Python as my chosen language. I have created two python scripts, 
one controlling  8 buttons.The second script runs the live stream option and button 9 on my blynk app 
is linked to my Glitch Application which then displays the livestream through a hyperlink you have chosen on the page.
I have set up a Bash Script that brings up a very small menu that helps you start the app and run the two python scripts
at the same time. To access the live stream you will need to click on the Marvel Mirror App button this brings you to a
glitch Application that has 4 pages. The first page is a gallery of the last 7 pictures you have taken. These photos are
being stored in the firebase Database. I have created this website using a little bit of Javascript which contains a small 
amount of html. I have used html and css to design the page. I decided since this app is mostly mobile based to design the 
layout to look better on mobile. While I was trying to code this assignment I corrupted my sd card which was a bit of a 
nightmare so I would suggest backing up everything you do. So I had to wipe my sd and start from scratch again.
I realised the installations were the most time consuming part to get back up and running. It took me 4 hours to get back 
on track as I had luckily backed up the bulk of my project. I have used multiple libraries tweepy to help send my tweets, 
twilio to send text if motion is detected.smtplib to send emails and of course the Blynklib so I can link up to my blynk app. 
I have used my senseHat to display a love heart design you can turn on and off with a blynk button.
I have used the sense hat to pick up temp humidity and pressure and will send back quotes if the conditions are met.
I have constructed a mirror that will be able to take a picture and send to twitter, email and also the firebase database 
and update on my glitch App gallery where it is timestamped. I decided to add one last button to my app that would act like 
a photobooth button as I got an early xmas present of a wifi printer, so I wanted to see what magic I could do with python. 
I installed cups so that my raspberry pi would recognise my printer. This took me quite a while to find the right documentation
to make it work but I am very happy with the outcome. This button acts as a polaroid, the images taken is printed straight away 
the image is not stored in firebase. On my app i also have a datastream that keeps track of temperature and displays both on
gauge and temperature graph. I have included a rgb zebra widget to add a bit of colour to my app it is also
handy as a colour picker.

To construct the mirror I bought a frame and I cut out holes the right size so the camera and sense_hat 
could only be seen from the front. I used a two way roll out mirror and wrapped it around the board from the frame 
and then put the frame back on . I then made sure my Raspberry pi was safe by making a case out of cardboard cause
I didn’t have a case so as not to short circuit the motherboard. I then attached it to the back so it could be visible 
and functional from the front. I shall attach a step by step constructional document.
   
referencing
https://stackoverflow.com/questions/3004811/how-do-you-run-multiple-programs-in-parallel-from-a-bash-script 
https://iotdesignpro.com/projects/sending-smtp-email-using-raspberry-pi 
https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/ 
https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3 
https://www.geeksforgeeks.org/python-send-sms-using-twilio/ 
https://uk.mathworks.com/help/thingspeak/embed-your-thingspeak-plots-on-web-pages.html  
https://www.w3schools.com/css/css_text.asp 
https://www.geeksforgeeks.org/how-to-append-html-code-to-a-div-using-javascript/ 
https://stackoverflow.com/questions/1184123/is-it-possible-to-add-dynamically-named-properties-to-javascript-object 
https://firebase.google.com/docs/storage/web/list-files 
https://www.twilio.com/docs/sms/send-messages#include-media-in-your-messages 
https://randomnerdtutorials.com/raspberry-pi-motion-detector-photo-capture/ 
https://www.reddit.com/r/raspberry_pi/comments/k7redu/testing_a_motion_detectionalert_system_i_made/ 
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals 
https://www.w3schools.com/jsref/met_doc_write.asp 
https://forum.freecodecamp.org/t/function-after-foreach-end/251589 
https://firebase.google.com/docs/storage/web/list-files 
https://cdnjs.com/libraries/semantic-ui 
https://pythonrepo.com/repo/resolator-rpi-surveillance 
https://himanshufi.medium.com/get-images-from-your-firebase-database-to-your-gallery-in-a-website-9f02efb41d33 
https://stackoverflow.com/questions/15148803/in-firebase-is-there-a-way-to-get-the-number-of-children-of-a-node-without-load 
https://stackoverflow.com/questions/18983138/callback-after-all-asynchronous-foreach-callbacks-are-completed 
https://masteringjs.io/tutorials/fundamentals/string-concat 
https://stackoverflow.com/questions/63342520/raspberry-pi-error-with-picamera-exc-picamerammalerror-failed-to-enable-connect 
https://stackoverflow.com/questions/56629793/importerror-lib-arm-linux-gnueabihf-libc-so-6-version-glibc-2-28-not-found 
https://www.mattcrampton.com/blog/step_by_step_tutorial_to_post_to_twitter_using_python_part_two-posting_with_photos/ 
https://blynk.io/blog/step-by-step-video-guide-to-making-your-first-project-on-new-blynk 
https://firebase.google.com/docs/auth/admin/errors 
https://raspberrypi.stackexchange.com/questions/67448/picamera-fails-after-a-while-out-of-resources-other-than-memory 
https://webhook.site/#!/2566394b-e278-4420-9712-e992778d6350/6def5f36-7359-44c4-8214-ef0206811dda/1 
https://picamera.readthedocs.io/en/release-1.10/recipes1.html 
https://stackoverflow.com/questions/12917224/capture-and-save-multiple-images-with-cameracapturedialog 
https://stackoverflow.com/questions/57475130/send-an-image-to-google-fire-base-using-python 
https://www.youtube.com/watch?v=UPQu3G_mzIs 
https://medium.com/@hugo__df/using-glitch-as-a-unix-command-line-playground-8e5cbdc9a8d5 
https://cdnjs.com/libraries/semantic-ui
https://stackoverflow.com/questions/48951939/printing-from-python-3-6-by-lp-lpr-not-recognised 
https://tutorials-raspberrypi.com/raspberry-pi-printer-setup-and-printing-images-by-pressing-button/ 
https://forums.raspberrypi.com/viewtopic.php?t=283350 
https://pypi.org/project/pycups/ 
https://www.techradar.com/how-to/computing/how-to-turn-the-raspberry-pi-into-a-wireless-printer-server-1312717/2 


