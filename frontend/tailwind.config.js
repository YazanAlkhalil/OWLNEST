/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
    },
    extend: {
      colors:{
        primary: "#001F34",
        secondary: '#3F6188',
        background: '#DBF2FF',
        accent: '#DEA01E',
        hover: '#182354'
      }
    },
  },
  plugins: [],
}

