import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
pirPin=6
GPIO.setup(pirPin,GPIO.IN)
counter=1
time.sleep(4)
a=1
while counter<=3:
    if GPIO.input(pirPin):
        print("motion detected")
        import os
        os.system("fswebcam -F 4 --fps 20 -r 1200*800 /home/pi/Desktop/"+str(a)+".jpg")
        print("pic taken")
        a=a+1
        time.sleep(1)
        counter=counter+1
print("testing")

        
