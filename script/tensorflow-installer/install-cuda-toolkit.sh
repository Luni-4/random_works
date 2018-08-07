# Install CUDA Toolkit through .run installer
# ./install-cuda-toolkit TOOLKIT VERSION [-u]

if [ "$3" = "-u" ]
then
  sudo /usr/local/cuda-$2/bin/uninstall_cuda_$2.pl
else
  chmod +x $1
  sudo $1 --override
fi
