# Install libcupti and set bashrc paths
# ./install-cupti-bashrc VERSION

sudo apt-get install libcupti-dev
echo "export PATH=/usr/local/cuda-$1/bin${PATH:+:${PATH}}" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}"  >> ~/.bashrc
