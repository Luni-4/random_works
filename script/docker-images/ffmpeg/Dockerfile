FROM ubuntu:bionic

MAINTAINER Luni-4 "https://github.com/Luni-4"

# Disable user-interaction
ENV DEBIAN_FRONTEND noninteractive

# List of FFmpeg packages
ENV FFMPEG="autoconf automake libtool build-essential \
cmake git-core pkg-config texinfo wget nasm \
python3-pip python3-setuptools python3-wheel \
libass-dev libfreetype6-dev libvorbis-dev libxcb1-dev libxcb-xfixes0-dev \
libsdl2-dev libvpx-dev libx264-dev libx265-dev libnuma-dev zlib1g-dev \
libwebp-dev libfdk-aac-dev libmp3lame-dev libopus-dev"

# Prepare building machine
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends -y \
        $FFMPEG

# Install meson and ninja
RUN pip3 install meson ninja

# Disable sslVerify
RUN git config --global http.sslVerify false

# Cleanup
RUN apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

# Install libaom
RUN git clone --depth 1 https://aomedia.googlesource.com/aom && \
    mkdir -p aom_build && \
    cd aom_build && \
    cmake \
        -G "Unix Makefiles" \
        -DENABLE_DOCS=off \
        -DENABLE_EXAMPLES=off \
        -DENABLE_NASM=on \
        -DBUILD_SHARED_LIBS=1 \
        -DENABLE_TESTDATA=off \
        -DENABLE_TESTS=off \
        ../aom && \
    make -j4 && \
    make install

RUN cd ..

# Build dav1d
RUN git clone --depth 1 https://code.videolan.org/videolan/dav1d.git && \
    cd dav1d && \
    meson build --buildtype release && \
    ninja -C build

RUN cd ..

# Install FFmpeg
RUN git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git && \
    cd /FFmpeg && \
    ./configure \
        --disable-debug \
        --disable-doc \
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
        --enable-libaom \
        --enable-libvpx \
        --enable-libx264 \
        --enable-libx265 \
        --enable-shared \
        --enable-version3 \
        --enable-nonfree && \
    make -j4 && \
    make install
