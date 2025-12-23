# gdrive_backup_commandline
============================================================
DEBIAN TO GOOGLE DRIVE BACKUP: STEP-BY-STEP GUIDE
============================================================

1. SYSTEM PREPARATION
---------------------
Run these commands to ensure your Debian system has the 
required tools installed:

   sudo apt update
   sudo apt install python3-venv rclone -y

2. R_CLONE CONFIGURATION (THE BRIDGE)
------------------------------------
You must link your Google Account to your terminal:

   a. Run: rclone config
   b. Type 'n' for New Remote.
   c. Name it: gdrive
   d. Select Option 18 (Google Drive).
   e. Leave Client ID and Client Secret BLANK (Press Enter).
   f. Scope: Select '1' (Full Access).
   g. Advanced Config: Type 'n'.
   h. Auto-Config: 
      - Type 'y' if you have a browser on this machine.
      - Type 'n' if you are using SSH (Headless).
   i. Follow the browser prompts to "Allow" rclone.
   j. Verify with: rclone lsd gdrive:

3. PYTHON ENVIRONMENT SETUP
---------------------------
Create a safe space for your script to run without 
interfering with Debian system files:

   mkdir ~/my_backup_project && cd ~/my_backup_project
   python3 -m venv venv
   source venv/bin/activate
   pip install keyring PyDrive2 google-api-python-client

4. RUNNING THE BACKUP SCRIPT
----------------------------
Every time you want to back up, follow these steps:

   a. Enter the folder: cd ~/my_backup_project
   b. Activate: source venv/bin/activate
   c. Run: python3 pythonbackup.py

   - The script will ask for an encryption password on 
     the first run. This stays in your CLI keyring.
   - For 'Source', enter: /home/michael
   - For 'Destination', enter: gdrive:MyBackupFolder

5. SECURITY NOTES
-----------------
- This method uses 'PlaintextKeyring' to avoid GUI 
  pop-ups. Your password is saved in a root-protected 
  local file (~/.local/share/python_keyring/).
- Never upload your 'venv' folder or 'credentials.json' 
  to GitHub.

============================================================
