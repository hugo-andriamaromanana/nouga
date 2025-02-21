from datetime import datetime
from pydantic import BaseModel

from nouga.ressources.youtube import YoutubeApi


class PlaylistHeader(BaseModel):
    id: str
    title: str
    description: str
    published_at: datetime
    last_updated: datetime
    len: int
