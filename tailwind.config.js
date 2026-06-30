/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
  ],
  theme: {
    extend: {
      colors: {
        'jht-dark': 'var(--color-primary)',
        'jht-gold': 'var(--color-accent)',
        'jht-gray': 'var(--color-bg)',
        'jht-gray-dark': 'var(--color-border)',
        'jht-blue-support': 'var(--color-text-secondary)',
      },
      fontFamily: {
        title: ['Montserrat', 'sans-serif'],
        sans: ['Open Sans', 'sans-serif'],
      },
      animation: {
        'marquee': 'marquee 30s linear infinite',
        'marquee-reverse': 'marqueeReverse 30s linear infinite',
        'vibrate-y': 'vibrate-y 0.4s ease-in-out',
        'fade-in-up': 'fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) both',
        'fade-in-slow': 'fadeInSlow 3.5s ease-out forwards',
        'takeoff': 'takeoff 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards',
        'counter': 'counterPulse 0.3s ease-out',
      },
      keyframes: {
        takeoff: {
          '0%': { transform: 'translate(0, 0) scale(1)', opacity: 1 },
          '20%': { transform: 'translate(-3px, 3px) scale(0.9)', opacity: 1 },
          '50%': { transform: 'translate(25px, -25px) scale(1.1)', opacity: 0 },
          '51%': { transform: 'translate(-25px, 25px) scale(0.8)', opacity: 0 },
          '100%': { transform: 'translate(0, 0) scale(1)', opacity: 1 },
        },
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        marqueeReverse: {
          '0%': { transform: 'translateX(-50%)' },
          '100%': { transform: 'translateX(0%)' },
        },
        'vibrate-y': {
          '0%, 100%': { transform: 'translateY(0)' },
          '25%': { transform: 'translateY(-6px)' },
          '50%': { transform: 'translateY(3px)' },
          '75%': { transform: 'translateY(-2px)' },
        },
        fadeInUp: {
          '0%': { opacity: '0', transform: 'translateY(40px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        fadeInSlow: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        },
        counterPulse: {
          '0%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.1)' },
          '100%': { transform: 'scale(1)' },
        },
      }
    },
  },
  plugins: [],
}
