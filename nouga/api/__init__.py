from fastapi import FastAPI, HTTPException

from nouga.ressources.youtube import YoutubeApi

app = FastAPI()

def update_playlists():
    # get playlists headers from db
    # get playlists headers from youtube
    # compare playlists headers, infer changes
    # update db


@app.post("/update")
def update_item():
    raise HTTPException(status_code=501, detail="Not Implemented")