
#!/bin/bash
echo ""
echo "Stopping services..."
systemctl stop status-check-button.service
systemctl stop status-check-lights.service

echo ""
echo "Starting services..."
systemctl daemon-reload
systemctl enable status-check-button.service
systemctl start status-check-button.service

systemctl enable status-check-lights.service
systemctl start status-check-lights.service