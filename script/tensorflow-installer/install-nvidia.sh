# Install Nvidia driver through .run installer
# ./install-nvidia PACKAGE [-u]

if [ "$2" = "-u" ]
then
  sudo $1 --uninstall
else
  chmod +x $1
  sudo $1
fi
