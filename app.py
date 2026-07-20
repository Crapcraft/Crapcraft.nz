import requests
import os
import json
from dotenv import load_dotenv 
load_dotenv() 

# jellyfin api urls/keys
JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
JF_HEADERS = {
    "Authorization": f'MediaBrowser Token="{JF_API}"'
}

#seerr api urls/keys
SEERR_URL = os.getenv("SEERR_URL")
SEERR_KEY = os.getenv("SEERR_KEY")
SEERR_HEADERS = {
    "X-API-Key": SEERR_KEY
}

#prowlarr api urls/keys
PROWLARR_URL = os.getenv("PROWLARR_URL")
PROWLARR_KEY = os.getenv("PROWLARR_KEY")
PROWLARR_HEADERS = {
    "X-API-Key": PROWLARR_KEY
}

#radarr api urls/keys
RADARR_URL = os.getenv("RADARR_URL")
RADARR_KEY = os.getenv("RADARR_KEY")
RADARR_HEADERS = {
    "X-API-Key": RADARR_KEY
}

#sonarr api urls/keys
SONARR_URL = os.getenv("SONARR_URL")
SONARR_KEY = os.getenv("SONARR_KEY")
SONARR_HEADERS = {
    "X-API-Key": SONARR_KEY
}

#lidarr api urls/keys
LIDARR_URL = os.getenv("LIDARR_URL")
LIDARR_KEY = os.getenv("LIDARR_KEY")
LIDARR_HEADERS = {
    "X-API-Key": LIDARR_KEY
}

#openwebui api url
OPENWEBUI_URL = os.getenv("OPENWEBUI_URL")


def jellyfin():
    response = requests.get(f"{JF_URL}/Items/Counts", headers=JF_HEADERS)
    data = response.json()
    return {
        "MovieCount": data["MovieCount"],
        "EpisodeCount": data["EpisodeCount"],
        "SongCount": data["SongCount"]
    }

def seerr():
    response = requests.get(f"{SEERR_URL}/api/v1/request/count", headers=SEERR_HEADERS)
    data = response.json()
    return {
        "RequestsTotal": data["total"],
        "RequestsPending": data["pending"],
        "RequestsApproved": data["approved"],
    }

def prowlarr():
    response = requests.get(f"{PROWLARR_URL}/api/v1/system/status", headers=PROWLARR_HEADERS)
    data = response.json()
    return {
        "ProwlarrVersion": data["version"],
    }

def radarr():
    response = requests.get(f"{RADARR_URL}/api/v3/system/status", headers=RADARR_HEADERS)
    data = response.json()
    return {
        "RadarrVersion": data["version"],
    }

def sonarr():
    response = requests.get(f"{SONARR_URL}/api/v3/system/status", headers=SONARR_HEADERS)
    data = response.json()
    return {
        "SonarrVersion": data["version"],
    }

def lidarr():
    response = requests.get(f"{LIDARR_URL}/api/v1/system/status", headers=LIDARR_HEADERS)
    data = response.json()
    return {
        "LidarrVersion": data["version"],
    }

def openwebui():
    response = requests.get(f"{OPENWEBUI_URL}/api/version")
    data = response.json()
    return {
        "OpenwebuiVersion": data["version"],
    }

def results():
    stats = {}
    stats.update(jellyfin())
    stats.update(seerr())
    stats.update(prowlarr())
    stats.update(radarr())
    stats.update(sonarr())
    stats.update(lidarr())
    stats.update(openwebui())

    with open("./website/stats.json", "w") as f:
        json.dump(stats, f)
        print(stats)
jellyfin()
seerr()
prowlarr()
radarr()
sonarr()
lidarr()
openwebui()
results()