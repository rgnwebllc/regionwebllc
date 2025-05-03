const messages = [
    "Building pixels with purpose...",
    "Hang tight, your site is almost ready.",
    "We craft. We code. We launch.",
    "Loading awesomeness...",
    "Launching RegionWeb magic...",
    "Grabbing assets.. (Probably)",
    "Defeating Pac-Man...",
  ];

  document.addEventListener("DOMContentLoaded", function () {
    // Set random loading message
    const randomIndex = Math.floor(Math.random() * messages.length);
    document.getElementById("loading-message").textContent = messages[randomIndex];

    // Remove preloader after full page load
    window.addEventListener("load", () => {
      const preloader = document.getElementById("preloader");
      if (preloader) {
        preloader.style.opacity = '0';
        preloader.style.transition = 'opacity 0.5s ease';
        setTimeout(() => preloader.style.display = 'none', 500);
      }
    });
  });