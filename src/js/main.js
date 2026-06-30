/**
 * JHT Transport — Main JavaScript
 * Vanilla JS — Sin dependencias externas
 * 
 * Funcionalidades:
 * 1. Intersection Observer (scroll-triggered animations)
 * 2. Contadores animados (Hero indicators)
 * 3. prefers-reduced-motion detection
 * 4. Lazy loading videos
 * 
 * ARQUITECTURA: Todo desacoplado.
 * Preparado para reemplazo por API calls en el futuro.
 * NO acoplar lógica de negocio aquí.
 */

(function () {
    'use strict';

    // ==========================================
    // 1. PREFERS-REDUCED-MOTION CHECK
    // ==========================================
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // ==========================================
    // 2. INTERSECTION OBSERVER — Scroll Animations
    // ==========================================
    function initScrollAnimations() {
        if (prefersReducedMotion) {
            // Si el usuario prefiere menos movimiento, mostrar todo directamente
            document.querySelectorAll('.scroll-trigger').forEach(function (el) {
                el.classList.add('is-visible');
            });
            return;
        }

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        document.querySelectorAll('.scroll-trigger').forEach(function (el) {
            observer.observe(el);
        });
    }

    // ==========================================
    // 3. CONTADORES ANIMADOS (Hero Indicators)
    // ==========================================
    function animateCounters() {
        var counters = document.querySelectorAll('[data-counter]');
        if (counters.length === 0) return;

        var counterObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var target = parseInt(entry.target.getAttribute('data-counter'), 10);
                    var duration = 2000; // 2 seconds
                    var startTime = null;

                    function animate(currentTime) {
                        if (!startTime) startTime = currentTime;
                        var progress = Math.min((currentTime - startTime) / duration, 1);
                        // Ease out cubic
                        var eased = 1 - Math.pow(1 - progress, 3);
                        var current = Math.floor(eased * target);

                        // Format with + suffix for large numbers
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
                        // Show final value immediately
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

    // ==========================================
    // 4. LAZY LOADING VIDEOS
    // ==========================================
    function initLazyVideos() {
        var videos = document.querySelectorAll('video[loading="lazy"]');
        if (videos.length === 0) return;

        var videoObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var video = entry.target;
                    // Force load the video source
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

    // ==========================================
    // INIT — Run when DOM is ready
    // ==========================================
    document.addEventListener('DOMContentLoaded', function () {
        initScrollAnimations();
        animateCounters();
        initLazyVideos();
    });

})();
