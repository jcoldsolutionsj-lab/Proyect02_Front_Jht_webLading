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

    // 5. Slot Machine Counters (Contadores numéricos suaves repetibles)
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const target = entry.target;
            
            if (entry.isIntersecting) {
                const targetValue = parseInt(target.getAttribute('data-counter'), 10);
                const duration = 2000; // 2 segundos (un poco más rápido)
                let startTimestamp = null;

                const step = (timestamp) => {
                    // Prevenir múltiples llamadas superpuestas
                    if (!target.dataset.animating) target.dataset.animating = "true";
                    
                    if (!startTimestamp) startTimestamp = timestamp;
                    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                    
                    // Curva de aceleración (easeOutExpo)
                    const easeOut = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
                    
                    const currentValue = Math.floor(easeOut * targetValue);
                    target.textContent = currentValue;
                    
                    if (progress < 1) {
                        target.animationFrame = window.requestAnimationFrame(step);
                    } else {
                        target.textContent = targetValue;
                        delete target.dataset.animating;
                    }
                };
                
                // Cancelar cualquier animación previa si entramos rápidamente
                if (target.animationFrame) cancelAnimationFrame(target.animationFrame);
                target.animationFrame = window.requestAnimationFrame(step);
                
            } else {
                // Cuando sale de la pantalla, lo reseteamos a 0 para que vuelva a rodar al entrar
                if (target.animationFrame) cancelAnimationFrame(target.animationFrame);
                delete target.dataset.animating;
                target.textContent = '0';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('[data-counter]').forEach(counter => {
        counterObserver.observe(counter);
    });
});

// 4. AlpineJS Global Components
document.addEventListener('alpine:init', () => {
    Alpine.data('typewriter', (fullText) => ({
        text: fullText,
        fullText: fullText,
        charIndex: fullText.length,
        isDeleting: true,
        type() {
            if (this.isDeleting) {
                this.charIndex -= 2;
                if(this.charIndex < 0) this.charIndex = 0;
            } else {
                this.charIndex++;
            }
            this.text = this.fullText.substring(0, this.charIndex) + (this.charIndex < this.fullText.length ? '|' : '');
            
            let typeSpeed = this.isDeleting ? 10 : 25;
            
            if (!this.isDeleting && this.charIndex >= this.fullText.length) {
                typeSpeed = 3000;
                this.isDeleting = true;
                this.text = this.fullText; // quita el cursor en pausa
            } else if (this.isDeleting && this.charIndex <= 0) {
                this.isDeleting = false;
                typeSpeed = 500;
            }
            setTimeout(() => this.type(), typeSpeed);
        },
        init() {
            setTimeout(() => this.type(), 3500);
        }
    }));
});
