import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='security_logs.log', level=logging.INFO)

# Log activity
def log_activity(user_id, action):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(f'{timestamp} - User {user_id} performed action: {action}')

# Example usage
if __name__ == "__main__":
    log_activity('123', 'Logged in')
