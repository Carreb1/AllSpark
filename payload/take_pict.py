# - To make it take photo at startup, use systemcmd
# -sudo nano /etc/systemd/system/takephoto.service
# [Unit]
# Description=Take photos at boot
# After=multi-user.target

# [Service]
# Type=simple
# ExecStart=/usr/bin/python3 /home/payload/take.py
# WorkingDirectory=/home/payload
# StandardOutput=append:/home/payload/takephoto.log
# StandardError=append:/home/payload/takephoto.log
# Restart=on-failure

# [Install]
# WantedBy=multi-user.target
# - sudo systemctl daemon-reload
# - sudo systemctl enable takephoto.service



from picamera2 import Picamera2
import time
import os

# Set the directory to save photos
save_dir = "/home/payload/pictures_cubesat"
os.makedirs(save_dir, exist_ok=True)  # Ensure the folder exists

# Initialize camera
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

picam2.start()
time.sleep(5)  # Let camera warm up

# Take 10 photos
for i in range(10):
    photo_path = os.path.join(save_dir, f"photo_on_boot{i}.png")
    try:
        picam2.capture_file(photo_path)
        print(f"PHOTO OK: {photo_path}")
    except Exception as e:
        print(f"Failed to save {photo_path}: {e}")
    time.sleep(1)

print("All photos saved.")
picam2.close()
