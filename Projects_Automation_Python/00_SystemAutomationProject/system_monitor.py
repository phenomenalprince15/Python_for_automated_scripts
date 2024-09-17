import psutil
import time
import subprocess
from logger import setup_logger
from backup_handler import create_backup

# Set up logger
logger = setup_logger()

def monitor_system(source_dir):
    logger.info("Starting system monitoring...")
    
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        mem_usage = psutil.virtual_memory().percent

        logger.info(f"CPU Usage: {cpu_usage}%, Memory Usage: {mem_usage}%")

        if cpu_usage > 50:
            logger.warning("High CPU usage detected, starting backup...")
            result = create_backup(source_dir)
            logger.info(result)
            notify_user(result)
        
        # Wait for 10 seconds before checking again
        time.sleep(10)

def notify_user(message):
    print(f"Notification: {message}")
    logger.info(f"Notification sent: {message}")

if __name__ == '__main__':
    # Specify the directory you want to back up
    source_directory = 'path_to_your_directory'
    monitor_system(source_directory)
