fetch("./stats.json")
    .then(response => response.json())
    .then(data => {
      document.getElementById("movie-count").textContent = data.MovieCount;
      document.getElementById("series-count").textContent = data.EpisodeCount;
      document.getElementById("song-count").textContent = data.SongCount;
      document.getElementById("requests-total").textContent = data.RequestsTotal;
      document.getElementById("requests-pending").textContent = data.RequestsPending;
      document.getElementById("requests-approved").textContent = data.RequestsApproved;
      document.getElementById("prowlarr-version").textContent = data.ProwlarrVersion;
      document.getElementById("radarr-version").textContent = data.RadarrVersion;
      document.getElementById("sonarr-version").textContent = data.SonarrVersion;
      document.getElementById("lidarr-version").textContent = data.LidarrVersion;
      document.getElementById("bazarr-version").textContent = data.BazarrVersion;
      document.getElementById("openwebui-version").textContent = data.OpenwebuiVersion;
      document.getElementById("qbittorrent-version").textContent = data.QbittorrentVersion;
      document.getElementById("tracearr-sessions").textContent = data.TotalSessions;
      document.getElementById("tracearr-streams").textContent = data.ActiveStreams;
      document.getElementById("tracearr-users").textContent = data.TotalUsers;
      document.getElementById("immich-photos").textContent = data.Photos;
      document.getElementById("immich-videos").textContent = data.Videos;
    });