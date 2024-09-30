import psutil
import smtplib

# Simple anomaly detection based on high CPU usage
def detect_intrusion():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:  # Threshold for potential intrusion
        alert_admin(cpu_usage)

# Alert system administrator via email
def alert_admin(cpu_usage):
    sender = "alert@cloudsecurity.com"
    receiver = "admin@cloudsecurity.com"
    message = f"Subject: Intrusion Alert\n\nHigh CPU usage detected: {cpu_usage}%"
    
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender, "password")
        server.sendmail(sender, receiver, message)

# Schedule intrusion detection check
if __name__ == "__main__":
    detect_intrusion()
