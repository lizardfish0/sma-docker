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
ENV SMA_RS Sonarr
ENV SMA_UPDATE false

RUN \
  # install
  apt-get update && \
  apt-get install -y \
    git \
    wget \
    xz-utils \
    python3 \
    python3-pip \
    python3-venv \
  # cleanup
  apt-get purge --auto-remove -y && \
  apt-get clean && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/*; && \
  # make sma directory
  mkdir ${SMA_PATH} && \
  # clone sma
  git config --global --add safe.directory ${SMA_PATH} && \
  git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git ${SMA_PATH}

EXPOSE 8989

VOLUME /config
VOLUME /usr/local/sma/config

# update.py sets FFMPEG/FFPROBE paths, updates API key and Sonarr/Radarr settings in autoProcess.ini
COPY extras/ ${SMA_PATH}/
COPY root/ /