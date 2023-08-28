#!/usr/bin/env python3


#import pihole as ph

#pihole = ph.PiHole("192.168.11.125")
#pihole.refresh()

#pihole.authenticate("Gypsum1980")
#pihole.disable(60)

#pihole.refresh()

#print(pihole.status)
#print(pihole.getVersion())
#print(pihole.gravity_last_updated)


import urllib.request, urllib.error, urllib.parse#!/usr/bin/env python3


f = urllib.request.urlopen('http://192.168.11.125/admin/api.php?disable=60&auth=bf24d2aa74054bb73b640c7bcbb111255e1a573fb308f9e0deaade9017e4f0b2')
f.close()