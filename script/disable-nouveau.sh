# Blacklist nouveau
sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"

# Check file content
cat /etc/modprobe.d/blacklist-nvidia-nouveau.conf

# Update initramfs
sudo update-initramfs -u

# Reboot
sudo reboot
