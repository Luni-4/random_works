# Install cudnn package on Ubuntu
# ./install-cudnn cudnn package cudnn package version

# Unpack cudnn-x.y archive
tar -zxvf $1

# Move the unpacked contents to the CUDA directory
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-$2/lib64/
sudo cp  cuda/include/cudnn.h /usr/local/cuda-$2/include/

# Give read access to all users
sudo chmod a+r /usr/local/cuda-$2/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
