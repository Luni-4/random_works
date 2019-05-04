FROM ubuntu:bionic

MAINTAINER Luni-4 "https://github.com/Luni-4"

# Disable user-interaction
ENV DEBIAN_FRONTEND noninteractive

# List of FFmpeg packages
ENV FFMPEG=" autoconf automake libtool build-essential \
cmake git-core pkg-config texinfo wget nasm \
libass-dev libfreetype6-dev libvorbis-dev libxcb1-dev libxcb-xfixes0-dev \
libsdl2-dev libvpx-dev libx264-dev libx265-dev libnuma-dev zlib1g-dev \
libwebp-dev libfdk-aac-dev libmp3lame-dev libopus-dev"

# Prepare building machine
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends -y \
        $FFMPEG

# Disable sslVerify        
RUN git config --global http.sslVerify false

# TODO install libaom

# TODO install david

# Install FFmpeg
RUN git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git && \
    cd /FFmpeg && \
    ./configure \
        --disable-debug \
        --disable-stripping \
        --disable-libdrm \
        --disable-cuda \
        --enable-avisynth \
        --enable-fontconfig \
        --enable-gpl \
        --enable-libass \
        --enable-libfdk-aac \
        --enable-libfreetype \
        --enable-libmp3lame \
        --enable-libopus \
        --enable-libvorbis \
        --enable-libvpx \
        --enable-libx264 \
        --enable-libx265 \
        --enable-shared \
        --enable-version3 \
        --enable-nonfree && \
    make -j4 && \
    make install
