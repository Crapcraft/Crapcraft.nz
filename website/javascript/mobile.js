(function() {
  const isMobile = /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

  if (isMobile && location.hostname !== 'm.crapcraft.nz') {
    window.location.href = 'https://m.crapcraft.nz';
  }
})();