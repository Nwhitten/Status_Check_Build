#!/usr/bin/env python3


# Import the library
import pihole as ph

pihole = ph.PiHole("192.168.11.125")
pihole.refresh()

pihole.authenticate("poolloop")
pihole.disable(60)

#pihole.refresh()

#print(pihole.status)
#print(pihole.getVersion())
#print(pihole.gravity_last_updated)
