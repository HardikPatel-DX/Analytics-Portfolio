// GSAP Animation
document.addEventListener("DOMContentLoaded", function() {
    gsap.from("#home h1", { opacity: 0, y: -50, duration: 1 });
    gsap.from("#home p", { opacity: 0, y: 20, duration: 1, delay: 0.5 });
    gsap.from("#about h2", { opacity: 0, y: -50, duration: 1, delay: 1 });
    gsap.from("#about p", { opacity: 0, y: 20, duration: 1, delay: 1.5 });
    gsap.from("#projects h2", { opacity: 0, y: -50, duration: 1, delay: 2 });
    gsap.from("#projects .project", { opacity: 0, y: 20, duration: 1, delay: 2.5, stagger: 0.3 });
    gsap.from("#contact h2", { opacity: 0, y: -50, duration: 1, delay: 3 });
    gsap.from("#contact p", { opacity: 0, y: 20, duration: 1, delay: 3.5 });

    // Strength hover effect for tooltip
    const strengths = document.querySelectorAll('.strength');
    
    strengths.forEach(strength => {
        strength.addEventListener('mouseenter', function () {
            const skillName = this.getAttribute('data-skill');
            const skillLevel = this.getAttribute('data-level');
            this.setAttribute('title', `${skillName} (Level: ${skillLevel})`);
        });
        
        strength.addEventListener('mouseleave', function () {
            this.removeAttribute('title');
        });
    });
    
    // Heatbar and marker positioning based on skill level
    strengths.forEach(strength => {
        const level = strength.getAttribute('data-level');
        const heatbar = strength.querySelector('.heatbar-container');
        const marker = heatbar.querySelector('.level-marker');
        
        // Set the marker position based on level (1 to 10)
        const levelPercent = level * 10; // 10% per level
        marker.style.left = `calc(${levelPercent}% - 10px)`; // Adjust positioning for center
        
        // Set the marker text
        marker.innerText = level;
    });
});

// Smooth Scroll
var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 800,
    speedAsDuration: true
});
