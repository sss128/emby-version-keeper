import os

import jq
import requests
from dotenv.main import load_dotenv

load_dotenv()
ember_server = os.environ.get("EMBY_SERVER")
token = os.environ.get("TOKEN")


def get_emby_libraries():
    r = requests.get(
        url=f"{ember_server}/emby/Library/VirtualFolders/Query?X-Emby-Token={token}",
        headers={"Content-Type": "application/json"},
    )
    res = jq.compile(
        r".Items | .[] | {name: .Name, locations: .Locations}"
    ).input_value(r.json())
    return filter(lambda x: any(x["locations"]), res.all())


def merge_emby_versions(emby_ids):
    requests.post(
        url=f"{ember_server}/emby/Videos/MergeVersions?Ids={emby_ids}&X-Emby-Token={token}"
    )

def divide_emby_versions(emby_id):
    requests.post(
        url=f"{ember_server}/emby/Videos/{emby_id}/AlternateSources/Delete?X-Emby-Token={token}"
    )