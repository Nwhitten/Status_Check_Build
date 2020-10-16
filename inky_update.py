import os
import json
import urllib.request, urllib.error, urllib.parse
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
from datetime import datetime

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# get api data


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
  
  
font_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",28)
fontsm_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",19)
fontti_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",16)
fontex_Arial = ImageFont.truetype("/usr/share/fonts/ArialUnicode.ttf",11)

font_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",28)
fontsm_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",19)
fontti_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",16)
fontex_ArialB = ImageFont.truetype("/usr/share/fonts/ArialBold.ttf",11)

font = ImageFont.truetype(FredokaOne, 28)
fontsm = ImageFont.truetype(FredokaOne, 22)
fontti = ImageFont.truetype(FredokaOne, 14)
fontex = ImageFont.truetype(FredokaOne, 12)

now = datetime.now()
current_time = now.strftime("%H:%M")

inky_display = InkyPHAT("red")
#inky_display = InkyPHAT("black")

inky_display.set_border(inky_display.WHITE)

if  str(holestatus) == 'enabled':
	img = Image.open("/usr/local/bin/status_check/background_pihole_sm.png")
	draw = ImageDraw.Draw(img)
	status_output = 'Enabled'
	status_output_w, status_output_h = font_ArialB.getsize(status_output)
	status_output_x = int((inky_display.WIDTH - status_output_w) / 2)
	draw.text((status_output_x,0), status_output, inky_display.BLACK, font_ArialB)
else:
	img = Image.new("P", (212, 104))
	draw = ImageDraw.Draw(img)
	status_output = 'Disabled'
	status_output_w, status_output_h = font_ArialB.getsize(status_output)
	status_output_x = int((inky_display.WIDTH - status_output_w) / 2)
	y_top = int(30)
	for y in range(0, y_top):
		for x in range(0, inky_display.width):
			img.putpixel((x, y), inky_display.RED)
	draw.text((status_output_x,0), status_output,inky_display.WHITE,font_ArialB)

draw.text((0,30), 'Total queries (' + str(unique_clients) + ' clients)      ' , inky_display.BLACK, fontex_ArialB)
draw.text((5,39), str(dns_queries) , inky_display.BLACK, fontti_ArialB)

draw.text((0,53), 'Queries Blocked        ' , inky_display.BLACK, fontex_ArialB)
draw.text((5,62), str(adsblocked) , inky_display.BLACK, fontti_ArialB)

draw.text((115,53), 'Percent Blocked        ' , inky_display.BLACK, fontex_ArialB)
draw.text((120,62), str("%.1f" % round(ratioblocked,2)) + "% ", inky_display.BLACK, fontti_ArialB)

draw.text((0,76), 'Domains on Blocklist        ' , inky_display.BLACK, fontex_ArialB)
draw.text((5,85), str(blocked_domains), inky_display.BLACK, fontti_ArialB)

draw.text((120,85),str(current_time), inky_display.RED, fontti_ArialB)


inky_display.set_image(img)

inky_display.show()
