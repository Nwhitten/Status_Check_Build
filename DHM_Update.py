import os
import json
import urllib.request, urllib.error, urllib.parse
import PIL
from displayhatmini import DisplayHATMini
from PIL import Image, ImageFont, ImageDraw
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

now = datetime.now()
current_time = now.strftime("%H:%M")

width = DisplayHATMini.WIDTH
height = DisplayHATMini.HEIGHT

while True:

	if  str(holestatus) == 'enabled':
		img = Image.open("/usr/local/bin/status_check/DHM_pihole.jpg")
		draw = ImageDraw.Draw(img)
		displayhatmini = DisplayHATMini(img)
		status_output = 'Enabled'
		status_output_w, status_output_h = font_ArialB.getsize(status_output)
		status_output_x = int((width - status_output_w) / 2)

		draw.text((status_output_x,0), status_output, (0,0,0), font_ArialB)
	else:
		img = Image.new("RGB", (width, height))
		draw = ImageDraw.Draw(img)
		displayhatmini = DisplayHATMini(img)
		status_output = 'Disabled'
		status_output_w, status_output_h = font_ArialB.getsize(status_output)
		status_output_x = int((width - status_output_w) / 2)
	
	
		draw.rectangle((0, 0, width, 50), (255, 0, 0))	
		draw.text((status_output_x,0), status_output,(255,255,255),font_ArialB)

	draw.text((0,30), 'Total queries (' + str(unique_clients) + ' clients)      ' , (0,0,0), fontex_ArialB)
	draw.text((5,39), str(dns_queries) , (0,0,0), fontti_ArialB)

	draw.text((0,53), 'Queries Blocked        ' , (0,0,0), fontex_ArialB)
	draw.text((5,62), str(adsblocked) , (0,0,0), fontti_ArialB)

	draw.text((115,53), 'Percent Blocked        ' , (0,0,0), fontex_ArialB)
	draw.text((120,62), str("%.1f" % round(ratioblocked,2)) + "% ", (0,0,0), fontti_ArialB)

	draw.text((0,76), 'Domains on Blocklist        ' , (0,0,0), fontex_ArialB)
	draw.text((5,85), str(blocked_domains), (0,0,0), fontti_ArialB)

	draw.text((120,85),str(current_time), (255,0,0), fontti_ArialB)

	displayhatmini.display()
	time.sleep(0.001)
