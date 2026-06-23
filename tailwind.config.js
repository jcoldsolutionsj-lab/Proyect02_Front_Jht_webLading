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
        'marquee': 'marquee 25s linear infinite',
        'vibrate-y': 'vibrate-y 0.4s ease-in-out',
        'fade-in-up': 'fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) both',
        'fade-in-slow': 'fadeInSlow 3.5s ease-out forwards',
      },
      keyframes: {
        marquee: {
          '0%': { transform: 'translateX(0%)' },
          '100%': { transform: 'translateX(-50%)' },
        },
        'vibrate-y': {
          '0%, 100%': { transform: 'translateY(0)' },
          '25%': { transform: 'translateY(-6px)' },
          '50%': { transform: 'translateY(3px)' },
          '75%': { transform: 'translateY(-2px)' },
        },
        fadeInSlow: {
          '0%': { opacity: 0 },
          '100%': { opacity: 1 },
        }
      }
    },
  },
  plugins: [],
}
