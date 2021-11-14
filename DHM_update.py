#!/usr/bin/env python3
import sys
import os
import json
import urllib.request, urllib.error, urllib.parse#!/usr/bin/env python3
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import ST7789
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

font_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",30)
fontti_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",25)
fontex_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",20)


try:
    f = urllib.request.urlopen('http://pihole.local/admin/api.php')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    adsblocked = parsed_json['ads_blocked_today']
    ratioblocked = parsed_json['ads_percentage_today']
    holestatus = parsed_json['status']
  
    dns_queries_today = parsed_json['dns_queries_today']
    unique_clients  = parsed_json['unique_clients']
    dns_queries  = parsed_json['dns_queries_all_types']
    blocked_domains  = parsed_json['domains_being_blocked']
  
    f.close()
except:
    queries = '?'
    adsblocked = '?'
    ratio = '?'

if  str(holestatus) == 'enabled':
    img = Image.open("/usr/local/bin/status_check/DHM_pihole_dark.jpg")
    draw = ImageDraw.Draw(img)
    status_output = 'Enabled'
    status_output_w, status_output_h = font_ArialB.getsize(status_output)
    status_output_x = int((width - status_output_w) / 2)
    draw.text((status_output_x,0), status_output, (0,0,0), font_ArialB)
  
else:
    img = Image.new("RGB",(width,height),(0,0,0))
    draw = ImageDraw.Draw(img)
    status_output = 'Disabled'
    status_output_w, status_output_h = font_ArialB.getsize(status_output)
    status_output_x = int((width - status_output_w) / 2)
    draw.rectangle((0, 0, width, status_output_h+4), (255, 0, 0))
    draw.text((status_output_x,0), status_output, (254,254,254), font_ArialB)

now = datetime.now()
current_time = now.strftime("%H:%M")

draw.text((0,40), 'Total queries (' + str(unique_clients) + ' clients)      ' , (200,200,200), fontex_ArialB)
draw.text((5,60), str(dns_queries) , (255,255,255), fontti_ArialB)

draw.text((0,90), 'Queries Blocked' , (200,200,200), fontex_ArialB)
draw.text((5,110), str(adsblocked) , (255,255,255), fontti_ArialB)

draw.text((0,140), 'Percent Blocked' , (200,200,200), fontex_ArialB)
draw.text((5,160), str("%.1f" % round(ratioblocked,2)) + "% ", (255,255,255), fontti_ArialB)

draw.text((0,190), 'Domains on Blocklist' , (200,200,200), fontex_ArialB)
draw.text((5,210), str(blocked_domains), (255,255,255), fontti_ArialB)

draw.text((250,210),str(current_time), (200,200,255), fontti_ArialB)
disp.display(img)

