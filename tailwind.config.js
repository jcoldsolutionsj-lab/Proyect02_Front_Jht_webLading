/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'jht-dark': '#1A3B6B',
        'jht-gold': '#FFD400',
        'jht-gray': '#E3E4E5',
        'jht-gray-dark': '#909AB3',
        'jht-blue-support': '#57678E',
      },
      fontFamily: {
        title: ['Montserrat', 'sans-serif'],
        sans: ['Open Sans', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
