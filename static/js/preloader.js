const messages = [
    "Building pixels with purpose...",
    "Hang tight, your site is almost ready.",
    "We craft. We code. We launch.",
    "Loading awesomeness...",
    "Launching RegionWeb magic...",
    "Grabbing assets.. (Probably)",
    "Defeating Pac-Man...",
    "Feeding the hamsters powering the servers...",
    "Teaching the CSS to behave...",
    "Untangling spaghetti code (again)...",
    "Asking ChatGPT for a hand...",
    "Googling how to center a div...",
    "Bribing the deploy gnomes...",
    "Running with scissors (don't worry, it's safe here)...",
    "Wrestling bugs into submission...",
    "Trying to remember our Git password...",
    "Telling the internet to be patient...",
    "Assembling the Avengers (for your website)...",
    "Using the Force to deploy...",
    "Waiting for Gandalf to finish the build...",
    "Summoning Dr. Strange’s portal to production...",
    "Adding a pinch of Wakandan vibranium...",
    "Spinning up the Spider-Verse...",
    "Running tests... 10% Tony Stark, 90% panic.",
    "Contacting R2-D2 for system diagnostics...",
    "Charging the Batmobile with CSS...",
    "Asking Yoda for performance tips... 'Fast it must be.'",
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