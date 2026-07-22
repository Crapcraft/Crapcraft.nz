#importing and loading

import requests
import os
import json
from dotenv import load_dotenv 
load_dotenv() 

#grabs the url and api key from .env and sets them as variables
#uses the JF_API variable to add the api key to JF_HEADERS so the api will accept the requests
JF_URL = os.getenv("JF")
JF_API = os.getenv("JF_KEY")
JF_HEADERS = {
    "Authorization": f'MediaBrowser Token="{JF_API}"'
}

#grabs the url and api key from .env and sets them as variables
#uses the SEERR_KEY variable to add the api key to SEERR_HEADERS so the api will accept the requests
SEERR_URL = os.getenv("SEERR_URL")
SEERR_KEY = os.getenv("SEERR_KEY")
SEERR_HEADERS = {
    "X-API-Key": SEERR_KEY
}

#grabs the url and api key from .env and sets them as variables
#uses the PROWLARR_KEY variable to add the api key to PROWLARR_HEADERS so the api will accept the requests
PROWLARR_URL = os.getenv("PROWLARR_URL")
PROWLARR_KEY = os.getenv("PROWLARR_KEY")
PROWLARR_HEADERS = {
    "X-API-Key": PROWLARR_KEY
}

#grabs the url and api key from .env and sets them as variables
#uses the RADARR_KEY variable to add the api key to RADARR_HEADERS so the api will accept the requests
RADARR_URL = os.getenv("RADARR_URL")
RADARR_KEY = os.getenv("RADARR_KEY")
RADARR_HEADERS = {
    "X-API-Key": RADARR_KEY
}

#grabs the url and api key from .env and sets them as variables
#uses the RADARR_KEY variable to add the api key to RADARR_HEADERS so the api will accept the requests
SONARR_URL = os.getenv("SONARR_URL")
SONARR_KEY = os.getenv("SONARR_KEY")
SONARR_HEADERS = {
    "X-API-Key": SONARR_KEY
}

#grabs the url and api key from .env and sets them as variables
#uses the LIDARR_KEY variable to add the api key to LIDARR_HEADERS so the api will accept the requests
LIDARR_URL = os.getenv("LIDARR_URL")
LIDARR_KEY = os.getenv("LIDARR_KEY")
LIDARR_HEADERS = {
    "X-API-Key": LIDARR_KEY
}

#grabs the url and api key from .env and sets them as variables
#uses the BAZARR_KEY variable to add the api key to BAZARR_HEADERS so the api will accept the requests
BAZARR_URL = os.getenv("BAZARR_URL")
BAZARR_KEY = os.getenv("BAZARR_KEY")
BAZARR_HEADERS = {
    "X-API-Key": BAZARR_KEY
}

#grabs the openwebui url from the .env and sets it as a variable
OPENWEBUI_URL = os.getenv("OPENWEBUI_URL")

#grabs the url and api key from .env and sets them as variables
#uses the QBITTORRENT_KEY variable to add the api key to QBITTORRENT_HEADERS so the api will accept the requests
QBITTORRENT_URL = os.getenv("QBITTORRENT_URL")
QBITTORRENT_KEY = os.getenv("QBITTORRENT_KEY")
QBITTORRENT_HEADERS = {
    "Authorization": f"Bearer {QBITTORRENT_KEY}"  
}

#jellyfin function that grabs the url from variable and uses headers to insert the api key into the http/api request and then filters the data only keeping MovieCount EpisodeCount and SongCount
def jellyfin():
    response = requests.get(f"{JF_URL}/Items/Counts", headers=JF_HEADERS)
    data = response.json()
    return {
        "MovieCount": data["MovieCount"],
        "EpisodeCount": data["EpisodeCount"],
        "SongCount": data["SongCount"]
    }

#seerr function that when run querys the api and filters out results only keeping total, pending and approved
def seerr():
    response = requests.get(f"{SEERR_URL}/api/v1/request/count", headers=SEERR_HEADERS)
    data = response.json()
    return {
        "RequestsTotal": data["total"],
        "RequestsPending": data["pending"],
        "RequestsApproved": data["approved"],
    }

#prowlarr function that only currently grabs the current software version will replace with real stats like seerrs stats at some point
def prowlarr():
    response = requests.get(f"{PROWLARR_URL}/api/v1/system/status", headers=PROWLARR_HEADERS)
    data = response.json()
    return {
        "ProwlarrVersion": data["version"],
    }

#radarr function that only currently grabs the current software version will replace with real stats like seerrs stats at some point
def radarr():
    response = requests.get(f"{RADARR_URL}/api/v3/system/status", headers=RADARR_HEADERS)
    data = response.json()
    return {
        "RadarrVersion": data["version"],
    }

#sonarr function that only currently grabs the current software version will replace with real stats like seerrs stats at some point
def sonarr():
    response = requests.get(f"{SONARR_URL}/api/v3/system/status", headers=SONARR_HEADERS)
    data = response.json()
    return {
        "SonarrVersion": data["version"],
    }

#lidarr function that only currently grabs the current software version will replace with real stats like seerrs stats at some point
def lidarr():
    response = requests.get(f"{LIDARR_URL}/api/v1/system/status", headers=LIDARR_HEADERS)
    data = response.json()
    return {
        "LidarrVersion": data["version"],
    }

def bazarr():
    response = requests.get(f"{BAZARR_URL}/api/system/status", headers=BAZARR_HEADERS)
    status = response.json()["data"]
    return {
        "BazarrVersion": status.get("bazarr_version", "Unknown"),
    }

#openwebui function that only currently grabs the current software version will most likely replace with real stats like seerrs stats at some point
def openwebui():
    response = requests.get(f"{OPENWEBUI_URL}/api/version")
    data = response.json()
    return {
        "OpenwebuiVersion": data["version"],
    }

#qbittorrent function that only currently grabs the current software version will replace with real stats like seerrs stats at some point
def qbittorrent():
    response = requests.get(f"{QBITTORRENT_URL}/api/v2/app/version", headers=QBITTORRENT_HEADERS)
    return {
        "QbittorrentVersion": response.text,
    }

#function that grabs the data from the service functions and sets it in stats{}
def results():
    stats = {}
    stats.update(jellyfin())
    stats.update(seerr())
    stats.update(prowlarr())
    stats.update(radarr())
    stats.update(sonarr())
    stats.update(lidarr())
    stats.update(bazarr())
    stats.update(openwebui())
    stats.update(qbittorrent())

#sends the data in stats{} to a .json file at ./website/stats.json
#the reason it sends the data to ./website/stats.json is so caddy can serv the file as the root folder for caddy is ./website because it it was this folder the .env would be exposed
    with open("./website/stats.json", "w") as f:
        json.dump(stats, f)
        print(stats) #debugging will remove at some point

#runs all the functions
jellyfin()
seerr()
prowlarr()
radarr()
sonarr()
lidarr()
bazarr()
openwebui()
qbittorrent()
results()