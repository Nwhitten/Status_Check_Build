#!/bin/bash
systemctl stop status-check-button.service
systemctl stop status-check-lights.service

echo ""

echo "Downloading files..."

wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/update.sh
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/button.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky_update.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/DHM_update.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/status_lights.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/pi-stats.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/PiholeControl.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/all_pi_stats.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/all_pi_stats_DHM.py
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/restart_services.sh


wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/status-check-button.service
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/status-check-lights.service

wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/background.png
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/background_pihole.png
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/background_pihole_sm.png
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/background_stats.png

wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/DHM_cog.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/DHM_pihole.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/DHM_rasp.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/DHM_pihole_dark.jpg
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/DHM_rasp_dark.jpg

wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/ArialUnicode.ttf
wget https://raw.githubusercontent.com/nwhitten/Status_Check_Build/main/inky-hole_assets/ArialBold.ttf

echo ""

echo "Removing old files files..."
rm -r /usr/local/bin/status_check
rm /etc/systemd/system/status-check-button.service
rm /etc/systemd/system/status-check-lights.service
rm /usr/share/fonts/ArialUnicode.ttf
rm /usr/share/fonts/ArialBold.ttf

echo ""

mkdir /usr/local/bin/status_check/

echo "Moving files..."

mv update.sh /usr/local/bin/status_check/
mv button.py /usr/local/bin/status_check/
mv inky_update.py /usr/local/bin/status_check/
mv DHM_update.py /usr/local/bin/status_check/
mv status_lights.py /usr/local/bin/status_check/
mv PiholeControl.py /usr/local/bin/status_check/
mv all_pi_stats.py /usr/local/bin/status_check/
mv all_pi_stats_DHM.py /usr/local/bin/status_check/
mv restart_services.sh /usr/local/bin/status_check/


mv background.png /usr/local/bin/status_check/
mv background_pihole.png /usr/local/bin/status_check/
mv background_pihole_sm.png /usr/local/bin/status_check/
mv background_stats.png /usr/local/bin/status_check/

mv DHM_cog.jpg /usr/local/bin/status_check/
mv DHM_pihole.jpg /usr/local/bin/status_check/
mv DHM_rasp.jpg /usr/local/bin/status_check/
mv DHM_pihole_dark.jpg /usr/local/bin/status_check/
mv DHM_rasp_dark.jpg /usr/local/bin/status_check/

mv ArialUnicode.ttf /usr/share/fonts/
mv ArialBold.ttf /usr/share/fonts/

mv status-check-button.service /etc/systemd/system/
mv status-check-lights.service /etc/systemd/system/

echo ""

echo "Starting services..."
systemctl daemon-reload
systemctl enable status-check-button.service
systemctl start status-check-button.service

systemctl enable status-check-lights.service
systemctl start status-check-lights.service

#echo ""
#echo "Installing crontab..."
#(crontab -l; echo "*/10 * * * * python3 /usr/local/bin/status_check/inky_update.py";) | crontab -
