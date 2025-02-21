from functools import cached_property
from typing import Any
from googleapiclient.discovery import build
from pydantic import BaseModel

from nouga.schemas.playlist import PlaylistHeader


class YoutubeApi(BaseModel):
    key: str

    @cached_property
    def ressource(self) -> Any:
        return build("youtube", "v3", developerKey=self.key)
    
    def create_video_headers(self, playlist_id: str) -> list[dict]:
        headers = []
        page_token = None
        while True:
            request = self.ressource.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=page_token
            )
            response = request.execute()
            for item in response["items"]:
                id = item["snippet"]["resourceId"]["videoId"]
                title = item["snippet"]["title"]
                description = item["snippet"]["description"]
                published_at = item["snippet"]["publishedAt"]
                header = {
                    "id": id,
                    "title": title,
                    "description": description,
                    "published_at": published_at,
                }
                headers.append(header)
            page_token = response.get("nextPageToken")
            if not page_token:
                break
        return headers
    
    def create_playlist_headers(self, user_id: str) -> list[str]:
        request = self.ressource.playlists().list(part="id", channelId=user_id)
        response = request.execute()
        return [item["id"] for item in response["items"]]
    
    def create_playlist_header(self, id: str) -> PlaylistHeader:
        request = self.ressource.playlists().list(part="snippet,contentDetails", id=id)
        response = request.execute()
        item = response["items"][0]
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        published_at = item["snippet"]["publishedAt"]
        last_updated = item["snippet"]["publishedAt"]
        len = item["contentDetails"]["itemCount"]
        return PlaylistHeader(
            id=id,
            title=title,
            description=description,
            published_at=published_at,
            last_updated=last_updated,
            len=len,
        )    
