#!/usr/bin/env python3

import time
import unicornhat as uh

import json
import urllib.request, urllib.error, urllib.parse#!/usr/bin/env python3

import requests
import signal
import buttonshim
import subprocess

# Import the library
#import pihole as ph

#from blinkt import set_pixel, set_brightness, show, clear
uh.set_layout(uh.PHAT)

#blinkt.set_clear_on_exit()

def website_up(url):
    try:
        r = requests.get(url)
        return r.ok
    except:
        return False

import subprocess, platform
def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception as e:
        return False

    return True

Cr,Cg,Cb = 0,50,0
Gr,Gg,Gb = 0,70,0
Ar,Ag,Ab = 130,60,0
Rr,Rg,Rb = 255,0,0
RrX,RgX,RbX = 130,0,0

ExternalSource = True
HoleStatus = "enabled"
ParsedHoleStatus= "enabled"

uh.clear()

while True:
    uh.brightness(1)
    if pingOk('188.72.89.2'):

        #PiHole
        PixelNumber =0
        PixelRow =0
        uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
        uh.show()
        if website_up('http://192.168.11.125/admin/'):
            f = urllib.request.urlopen('http://192.168.11.125/admin/api.php?summaryRaw&auth=bf24d2aa74054bb73b640c7bcbb111255e1a573fb308f9e0deaade9017e4f0b2')
            json_string = f.read()
            parsed_json = json.loads(json_string)
            HoleStatusParsed = parsed_json['status']
            f.close()

            if str(HoleStatusParsed) == "enabled":
                uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
            else:
                uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
            uh.show()
            if not str(HoleStatusParsed) == HoleStatus:
                HoleStatus = str(HoleStatusParsed)
                exec(open("/usr/local/bin/status_check/DHM_update.py").read())
                #exec(open("/usr/local/bin/status_check/inky_update.py").read())
        else:
            uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
            uh.show()

        #HomeBridge Admin
        PixelNumber =1
        PixelRow =0
        uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
        uh.show()
        if website_up('http://192.168.11.160:8581/login'):
            uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
        else:
            uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
        uh.show()

        #CODEX ADMIN
        PixelNumber =3
        PixelRow =0
        uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
        uh.show()
        if website_up('http://192.168.11.190:3755/cgi-bin/'):
            uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
        else:
            uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
        uh.show()

        #Codex PLEX
        PixelNumber =4
        PixelRow =0
        uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
        uh.show()
        if website_up('http://192.168.11.190:32400/web/'):
            uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
        else:
            uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
        uh.show()

        
        
        
        
        if ExternalSource == True:
            
             #PiHole
            #PixelNumber =0
            #PixelRow =2
            #uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
            #uh.show()
            #if website_up('http://192.168.195.112/admin/'):
                #pihole = ph.PiHole("192.168.195.112")
                #pihole.refresh()
                #if pihole.status == "enabled":
                    #uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
                #else:
                    #uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
                #uh.show()
            #else:
                #uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
                #uh.show()
            
            
            
            
            
            
            #Jane Pi
            PixelNumber =3
            PixelRow =2
            uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
            uh.show()
            if pingOk('192.168.195.112'):
                uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
            else:
                uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
            uh.show()
            
            #Janie Plus PLEX
            PixelNumber =4
            PixelRow =2
            uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
            uh.show()
            if website_up('http://192.168.195.112:32400/web/'):
                uh.set_pixel(PixelNumber,PixelRow, Gr,Gg,Gb)
            else:
                uh.set_pixel(PixelNumber,PixelRow, Rr,Rg,Rb)
            uh.show()


            
    #Temp
        #buttonshim.set_pixel(0x94, 0x00, 0xd3)
        PixelNumber =7
        PixelRow =3
        uh.set_pixel(PixelNumber,PixelRow,Cr,Cg,Cb)
        #show()
        cmd ="cat /sys/class/thermal/thermal_zone0/temp"
        thermal = subprocess.check_output(cmd, shell=True).decode("utf8")
        tempC =  round(float(thermal) / 1e3,1)

        # Change backlight if temp changes
        #print(tempC)
        if tempC < 40:
        	uh.set_pixel(PixelNumber,PixelRow, 0,0,50)
            #buttonshim.set_pixel(0,0,200)
        elif tempC < 50:
        	uh.set_pixel(PixelNumber,PixelRow, 0,50,0)
            #buttonshim.set_pixel(0,200,0)
        elif tempC > 60:
        	uh.set_pixel(PixelNumber,PixelRow, 75,0,0)
            #buttonshim.set_pixel(255,0,0)
        else:
        	uh.set_pixel(PixelNumber,PixelRow, 50,50,0)
            #buttonshim.set_pixel(200,200,0)
        uh.show()

        #clear()
        #show()
        time.sleep(5)
    else:
        uh.brightness(1)
        uh.clear()
        
        uh.set_all(0,0,0)
        uh.show()
        time.sleep(1)
        uh.set_all(0,0,255)
        uh.show()
        time.sleep(1)
        uh.clear()
