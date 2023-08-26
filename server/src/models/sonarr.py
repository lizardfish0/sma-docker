from typing import Optional

from pydantic import BaseModel


class Series(BaseModel):
    id: int
    title: str
    path: str
    tvdbId: Optional[int] = None
    tvMazeId: Optional[int] = None
    imdbId: Optional[str] = None
    type: Optional[str] = None


class Episode(BaseModel):
    id: int
    episodeNumber: int
    seasonNumber: int
    title: str
    airDate: str
    airDateUtc: str


class EpisodeFile(BaseModel):
    id: int
    relativePath: str
    path: str
    quality: str
    qualityVersion: int
    releaseGroup: str
    size: int
    sceneName: Optional[str] = None


class SonarrWebhook(BaseModel):
    series: Series
    episodes: list[Episode]
    eventType: str
    episodeFile: Optional[EpisodeFile] = None
    isUpgrade: Optional[bool] = None
    downloadClient: Optional[str] = None
    downloadClientType: Optional[str] = None
    downloadId: Optional[str] = None
    deletedFiles: Optional[list[EpisodeFile]] = None
