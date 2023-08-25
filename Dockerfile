ARG ffmpeg_source=ghcr.io/linuxserver/ffmpeg
ARG ffmpeg_tag=latest

FROM ${ffmpeg_source}:${ffmpeg_tag} as ffmpeg
LABEL maintainer="lizardfish0 lizardfish0@protonmail.com"

ENV \
  LIBVA_DRIVERS_PATH="/usr/local/lib/x86_64-linux-gnu/dri" \
  LD_LIBRARY_PATH="/usr/local/lib" \
  NVIDIA_DRIVER_CAPABILITIES="compute,video,utility" \
  NVIDIA_VISIBLE_DEVICES="all"

ENV SMA_PATH /usr/local/sma
ENV SMA_SERVER_PATH /usr/local/sma-server

RUN \
    # install
    apt-get update && \
    apt-get install -y \
    git \
    python3 \
    python3-pip \
    python3-venv && \
    # cleanup
    apt-get purge --auto-remove -y && \
    apt-get clean && \
    rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/* && \
    # make sma directory
    mkdir ${SMA_PATH} && \
    # make sma-server directory
    mkdir ${SMA_SERVER_PATH} && \
    # clone sma
    git config --global --add safe.directory ${SMA_PATH} && \
    git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git ${SMA_PATH}

COPY sma/ ${SMA_PATH}
COPY server/ ${SMA_SERVER_PATH}
COPY root/ /

EXPOSE 9090
VOLUME /usr/local/sma/config

ENTRYPOINT ["/init"]