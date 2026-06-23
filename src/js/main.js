document.addEventListener('DOMContentLoaded', () => {
    // 1. Initial Page Load Animation
    document.body.classList.add('fade-in-load');

    // 2. Parallax Effect for Hero Background
    const parallaxBg = document.querySelector('.parallax-bg');
    if (parallaxBg) {
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            // Moves the background video 15% slower than the foreground
            parallaxBg.style.transform = `translateY(${scrollY * 0.15}px)`;
        }, { passive: true });
    }

    // 3. Scroll-Triggered Animations (Intersection Observer)
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // 15% of the element must be visible
    };

    const scrollObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Stop observing once animated so it only animates once
                observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.scroll-trigger');
    animatedElements.forEach(el => scrollObserver.observe(el));
});
