import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir='backup'):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(backup_dir, f'backup_{timestamp}')
    
    try:
        shutil.copytree(source_dir, backup_path)
        return f"Backup created successfully at {backup_path}"
    except Exception as e:
        return f"Failed to create backup: {e}"
