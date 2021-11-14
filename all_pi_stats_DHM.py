import os
import json
import urllib.request, urllib.error, urllib.parse
import socket
import sys
import ST7789
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime

# Create ST7789 LCD display class.

disp = ST7789.ST7789(
    height=240,
    width=320,
    rotation=180,
    port=0,
    cs=1,
    dc=9,
    backlight=13,
    spi_speed_hz=60 * 1000 * 1000,
    offset_left=0,
    offset_top=0)


# Initialize display.
disp.begin()

width = disp.width
height = disp.height


#ip_add = sys.argv[1]
ip_add = '192.168.11.160'

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("/usr/local/bin/status_check/DHM_cog.jpg")
draw = ImageDraw.Draw(img)

# get api data


try:
  f = urllib.request.urlopen('http://' + str(ip_add) + ':8089/monitor2.json')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  uptime = parsed_json['uptime']
  formatted_uptime = parsed_json['formatted_uptime']
  ip = parsed_json['ip']
  host_name = parsed_json['host_name']
  kernel_release = parsed_json['kernel_release']
  soc_temp = parsed_json['soc_temp']
  temp = parsed_json['temp']
  load_avg = parsed_json['load_avg']
  load_current = parsed_json['load_current']
  load_percent = parsed_json['load_percent']
  #memory_usage = parsed_json['memory_usage']
  memory_percent = parsed_json['memory_percent']
  disk_usage = parsed_json['disk_usage']
  disk_percent = parsed_json['disk_percent']
  f.close()
except:
  queries = '?'
  #adsblocked = '?'
  #ratio = '?'
  
font_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",28)
fontsm_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",19)
fontti_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",16)
fontex_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",11)

font_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",28)
fontsm_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",19)
fontti_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",16)
fontex_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",11)

now = datetime.now()
current_time = now.strftime("%H:%M")



draw.text((0,0), str(host_name),(0,0,0)),fontsm_ArialB)
draw.text((5,20), str(ip), (0,0,0), fontex_ArialB)

draw.text((5,38), str(formatted_uptime),(0,0,0),fontti_ArialB)
draw.text((5,53), str(temp) + chr(176) + "c", (0,0,0), fontti_ArialB)

draw.text((5,68), "C:" + str(load_percent) + "% ", (0,0,0), fontti_ArialB)
draw.text((75,68), "M:" + str(memory_percent) + "% ", (0,0,0), fontti_ArialB)

draw.text((5,83), "D:" + str(disk_usage) + " GB", (0,0,0), fontti_ArialB)
draw.text((155,83),str(current_time), (0,0,0), fontsm_ArialB)

disp.display(img)
