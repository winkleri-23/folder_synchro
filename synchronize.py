import os
import shutil
import time
import argparse
from datetime import datetime

def sync_folders(source_path, replica_path, log_file, interval_seconds):
    while True:
        try:
            # Sync folders
            sync_result = sync(source_path, replica_path)

            # Log to console
            print(f"[{datetime.now()}] {sync_result}")

            # Log to file
            with open(log_file, 'a') as log:
                log.write(f"[{datetime.now()}] {sync_result}\n")

            # Wait for the specified interval
            time.sleep(interval_seconds)

        except KeyboardInterrupt:
            print("Synchronization stopped by user.")
            break

def sync(source_path, replica_path):
    sync_result = ""

    # Check if source folder exists
    if not os.path.exists(source_path):
        return "Source folder does not exist."

    # Create replica folder if it doesn't exist
    if not os.path.exists(replica_path):
        os.makedirs(replica_path)
        sync_result += "Replica folder created. "

    # Sync files from source to replica
    for root, dirs, files in os.walk(source_path):
        relative_path = os.path.relpath(root, source_path)
        replica_root = os.path.join(replica_path, relative_path)

        # Sync directories
        for dir_name in dirs:
            replica_dir = os.path.join(replica_root, dir_name)
            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)
                sync_result += f"Created directory: {replica_dir}. "

        # Sync files
        for file_name in files:
            source_file = os.path.join(root, file_name)
            replica_file = os.path.join(replica_root, file_name)

            if not os.path.exists(replica_file) or os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                shutil.copy2(source_file, replica_file)
                sync_result += f"Copied file: {replica_file}. "

    return sync_result.strip()

def main():
    parser = argparse.ArgumentParser(description="Folder Synchronization Program")
    parser.add_argument("source_path", help="Path to the source folder")
    parser.add_argument("replica_path", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval_seconds", type=int, help="Synchronization interval in seconds")

    args = parser.parse_args()

    sync_folders(args.source_path, args.replica_path, args.log_file, args.interval_seconds)

if __name__ == "__main__":
    main()
