from dataclasses import dataclass


@dataclass
class Movie:
    id: str
    title: str
    year: int
    releaseDate: str
    folderPath: str
    tmdbId: int
    imdbId: str


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
class RadarrWebhook:
    movie: Movie
    remoteMovie: RemoteMovie
    movieFile: MovieFile
    isUpgrade: bool
    downloadClient: str
    downloadClientType: str
    downloadId: str
    eventType: str
