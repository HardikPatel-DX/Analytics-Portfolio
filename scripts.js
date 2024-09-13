// Ensure the DOM is fully loaded before executing scripts
document.addEventListener("DOMContentLoaded", function() {
    // GSAP Animation
    gsap.from("#home h1", { opacity: 0, y: -50, duration: 1 });
    gsap.from("#home p", { opacity: 0, y: 20, duration: 1, delay: 0.5 });
    gsap.from("#about h2", { opacity: 0, y: -50, duration: 1, delay: 1 });
    gsap.from("#about p", { opacity: 0, y: 20, duration: 1, delay: 1.5 });
    gsap.from("#projects h2", { opacity: 0, y: -50, duration: 1, delay: 2 });
    gsap.from("#projects .project", { opacity: 0, y: 20, duration: 1, delay: 2.5, stagger: 0.3 });
    gsap.from("#contact h2", { opacity: 0, y: -50, duration: 1, delay: 3 });
    gsap.from("#contact p", { opacity: 0, y: 20, duration: 1, delay: 3.5 });

    // Smooth Scrolling for anchor links using Smooth Scroll library
    const scroll = new SmoothScroll('a[href*="#"]', {
        speed: 600,
        speedAsDuration: true,
        offset: 70 // Adjust if you have a fixed navbar
    });
});
