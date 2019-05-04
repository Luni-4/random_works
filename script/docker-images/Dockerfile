FROM ubuntu:bionic

MAINTAINER rr- "https://github.com/rr-"

# Disable user-interaction
ENV DEBIAN_FRONTEND noninteractive

# List of MPV package
ENV MPV="libegl1-mesa libgl1-mesa-glx libice6 libsm6 libx11-xcb1 libx11-6 \
libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 \
libxinerama1 libxrandr2 libxrender1 libxss1 libxtst6 libxv1 libasound2 \
libbluray-dev libcaca0 libcdio-dev libcdio-cdda-dev libcdio-paranoia-dev \
libdvdnav4 libdvdread4 libenca0 \
libfontconfig1 libfreetype6 libgstreamer-plugins-base1.0-dev libguess1 \
libharfbuzz0b libicu60 libjack-jackd2-0 libjpeg-turbo8 liblua5.2-0 libpulse0 \
libpython3.4 librubberband2 libsmbclient libuchardet0 libv4l-0 libvdpau1 \
libwayland-egl1-mesa libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \
libxcb-randr0 libxcb-render-util0 libxcb-render0 \
libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxcb-xkb1 libxcb1 \
libxkbcommon-x11-0 libxkbcommon0 libgnutlsxx28 libmp3lame0 libopus0 \
libx264-152 libtheora0"

# List of bubblesub package
ENV BUBBLESUB="python3-pip python3-setuptools python3-wheel python-minimal \
fftw3 qt5-default"

# Prepare building machine
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends -y \
        $MPV $FFMS2 $BUBBLESUB

# Set Python
RUN rm -f /usr/bin/python && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    python -v



# Install mpv
#RUN git clone --depth 1 https://github.com/mpv-player/mpv.git && \
    #cd mpv && \
    #wget https://waf.io/waf-2.0.15 -O waf && \
    #chmod +x waf && \
    #./waf configure && \
    #./waf && \
    #./waf install

#RUN cd ..



# Install ffms2
#RUN git clone --depth 1 https://github.com/FFMS/ffms2.git && \
    #cd ffms2 && \
    #./autogen.sh && \
    #./configure.ac && \
    #make && \
    #make install

#RUN cd ..

# Install bubblesub
#RUN git clone --depth 1 https://github.com/rr-/bubblesub && \
    #cd bubblesub && \
    #pip3 install --user .

# Set the port used by the container
EXPOSE 4567
