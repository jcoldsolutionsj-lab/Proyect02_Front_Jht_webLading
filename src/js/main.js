/**
 * JHT Transport — Main JavaScript
 */

(function () {
    'use strict';

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function initScrollAnimations() {
        if (prefersReducedMotion) {
            document.querySelectorAll('.scroll-trigger').forEach(function (el) {
                el.classList.add('is-visible');
            });
            return;
        }

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    // We remove it from main so it re-animates, let's keep it from main.
                } else {
                    entry.target.classList.remove('is-visible');
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px'
        });

        document.querySelectorAll('.scroll-trigger').forEach(function (el) {
            observer.observe(el);
        });
    }

    function animateCounters() {
        var counters = document.querySelectorAll('[data-counter]');
        if (counters.length === 0) return;

        var counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var target = parseInt(entry.target.getAttribute('data-counter'), 10);
                    var duration = 2000;
                    var startTime = null;

                    function animate(currentTime) {
                        if (!startTime) startTime = currentTime;
                        var progress = Math.min((currentTime - startTime) / duration, 1);
                        var eased = 1 - Math.pow(1 - progress, 3);
                        var current = Math.floor(eased * target);

                        if (target >= 1000) {
                            entry.target.textContent = current.toLocaleString('es-PE') + '+';
                        } else {
                            entry.target.textContent = current + '+';
                        }

                        if (progress < 1) {
                            requestAnimationFrame(animate);
                        }
                    }

                    if (prefersReducedMotion) {
                        entry.target.textContent = target >= 1000
                            ? target.toLocaleString('es-PE') + '+'
                            : target + '+';
                    } else {
                        requestAnimationFrame(animate);
                    }

                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        counters.forEach(function (counter) {
            counterObserver.observe(counter);
        });
    }

    function initLazyVideos() {
        var videos = document.querySelectorAll('video[loading="lazy"]');
        if (videos.length === 0) return;

        var videoObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var video = entry.target;
                    var sources = video.querySelectorAll('source');
                    sources.forEach(function (source) {
                        if (source.dataset.src) {
                            source.src = source.dataset.src;
                        }
                    });
                    video.load();
                    videoObserver.unobserve(video);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '200px 0px'
        });

        videos.forEach(function (video) {
            videoObserver.observe(video);
        });
    }

    function initParallax() {
        const parallaxBg = document.querySelector('.parallax-bg');
        if (parallaxBg) {
            window.addEventListener('scroll', () => {
                const scrollY = window.scrollY;
                parallaxBg.style.transform = `translateY(${scrollY * 0.15}px)`;
            }, { passive: true });
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
        document.body.classList.add('fade-in-load');
        initScrollAnimations();
        animateCounters();
        initLazyVideos();
        initParallax();
    });

})();
