#!/bin/bash

LOG_FILE="security_logs.log"
ALERT_EMAIL="admin@cloudsecurity.com"

# Check for any suspicious activity in logs
grep "Intrusion" $LOG_FILE
if [ $? -eq 0 ]; then
    echo "Suspicious activity detected. Sending alert email..."
    echo "Suspicious activity found in logs" | mail -s "Alert: Suspicious Activity" $ALERT_EMAIL
else
    echo "No suspicious activity detected."
fi
