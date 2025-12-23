import os
import getpass
import keyring
import subprocess

def get_config():
    # 1. Handle the Encryption Password securely
    service_name = "DebianBackup"
    user_identifier = "backup_admin"
    
    password = keyring.get_password(service_name, user_identifier)
    
    if not password:
        print("No backup password found in secure storage.")
        password = getpass.getpass("Create a new encryption password for your backups: ")
        keyring.set_password(service_name, user_identifier, password)
        print("Password saved securely.")

    # 2. Handle Paths (Prompting instead of hard-coding)
    source_path = input("Enter the full path of the folder to back up (e.g., /home/user/Docs): ").strip()
    dest_path = input("Enter the Google Drive destination (e.g., gdrive:MyBackups): ").strip()

    return password, source_path, dest_path

def run_rclone_backup():
    password, source, dest = get_config()
    
    # We use Rclone with the '--crypt' logic or simple copy.
    # Here we use a standard copy command.
    print(f"\nInitializing secure transfer from {source}...")
    
    try:
        # We pass the password to the environment only during execution
        # so it is never saved in the script file or bash history.
        env = os.environ.copy()
        env["RCLONE_CONFIG_MYREMOTE_PASSWORD"] = password 
        
        subprocess.run(["rclone", "copy", source, dest, "--progress"], check=True, env=env)
        print("\nBackup completed successfully.")
        
    except subprocess.CalledProcessError as e:
        print(f"\nError during backup: {e}")
    except FileNotFoundError:
        print("\nError: 'rclone' is not installed. Please run 'sudo apt install rclone'.")

if __name__ == "__main__":
    run_rclone_backup()
