from dataclasses import dataclass
from typing import Optional

from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    year: int
    releaseDate: str
    folderPath: str
    tmdbId: Optional[int] = None
    imdbId: Optional[str] = None
    overview: Optional[str] = None


class RemoteMovie(BaseModel):
    tmdbId: int
    imdbId: str
    title: str
    year: int


class MovieFile(BaseModel):
    id: int
    relativePath: str
    path: str
    quality: str
    qualityVersion: int
    releaseGroup: str
    indexerFlags: str
    size: int
    dateAdded: Optional[str] = None
    mediaInfo: Optional[dict] = None
    sceneName: Optional[str] = None


class Release(BaseModel):
    quality: Optional[str] = None
    qualityVersion: Optional[int] = None
    releaseGroup: Optional[str] = None
    releaseTitle: Optional[str] = None
    indexer: Optional[str] = None
    size: Optional[int] = None
    customFormatScore: Optional[int] = None


class CustomFormat(BaseModel):
    id: int
    name: str


class CustomFormatInfo(BaseModel):
    customFormats: list[CustomFormat]
    customFormatScore: int


class RadarrWebhook(BaseModel):
    movie: Movie
    remoteMovie: RemoteMovie
    instanceName: str
    eventType: str
    customFormatInfo: Optional[CustomFormatInfo] = None
    isUpgrade: Optional[bool] = None
    movieFile: Optional[MovieFile] = None
    release: Optional[Release] = None
    deletedFiles: Optional[list[MovieFile]] = None
