#!/bin/bash
systemctl stop status-check-button.service
systemctl stop status-check-lights.service

echo ""


echo "Removing old files files..."
rm -r /usr/local/bin/status_check
rm /etc/systemd/system/status-check-button.service
rm /etc/systemd/system/status-check-lights.service
rm /usr/share/fonts/ArialMono.ttf
rm /usr/share/fonts/ArialBold.ttf

echo ""
