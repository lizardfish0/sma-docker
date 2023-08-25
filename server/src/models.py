from dataclasses import dataclass
from typing import Optional


@dataclass
class Movie:
    id: int
    title: str
    year: int
    releaseDate: str
    folderPath: str
    tmdbId: Optional[int] = None
    imdbId: Optional[str] = None


@dataclass
class RemoteMovie:
    tmdbId: int
    imdbId: str
    title: str
    year: int


@dataclass
class MovieFile:
    id: int
    relativePath: str
    path: str
    quality: str
    qualityVersion: int
    releaseGroup: str
    sceneName: str
    indexerFlags: str
    size: int


@dataclass
class Release:
    quality: str
    qualityVersion: int
    releaseGroup: str
    releaseTitle: str
    indexer: str
    size: int
    customFormatScore: int


@dataclass
class RadarrWebhook:
    movie: Movie
    remoteMovie: RemoteMovie
    instanceName: str
    eventType: str
    isUpgrade: Optional[bool] = None
    movieFile: Optional[MovieFile] = None
    release: Optional[Release] = None
