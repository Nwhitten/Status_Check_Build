
## Installation

### Automatic

`wget -O - https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/install.sh | sudo bash`


### Additional Requirements
need to run:

`(crontab -l; echo "*/10 * * * * python3 /usr/local/bin/status_check/inky_update.py";) | crontab -`
to install cron job to refresh pihole stats on inky-phat every 10 mins


`(crontab -l; echo "*/1 * * * * python3 /usr/local/bin/status_check/DHM_update.py";) | crontab -`
to install cron job to refresh pihole stats on Display HAT Mini every 1 min


you will also need to install the following:

Pi Monitor2
  `wget -O - https://raw.githubusercontent.com/nwhitten/pi_monitor/master/install2.sh | sudo bash`

Inky Phat library 
  `curl https://get.pimoroni.com/inky | bash`

OR

Display HAT Mini library
    
  `sudo apt update`

  `sudo raspi-config nonint do_spi 0`

  `sudo apt install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy`

  `sudo pip3 install st7789`
      

Unicorn Phat library 

    `curl -sS https://get.pimoroni.com/unicornhat | bash`

button shim library

    `curl https://get.pimoroni.com/buttonshim | bash`

PiHole-api

    `sudo python3 -m pip install --no-cache-dir PiHole-api`

zero tier

    `curl -s https://install.zerotier.com | sudo bash` (extra setup required)
