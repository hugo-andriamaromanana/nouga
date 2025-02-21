from dataclasses import dataclass
from datetime import datetime

@dataclass
class VideoHeader:
    id: str
    title: str
    description: str
    published_at: datetime