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
      }
    },
  },
  plugins: [],
}
