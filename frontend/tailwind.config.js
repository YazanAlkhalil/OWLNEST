/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  darkMode:'class',
  theme: {
    fontFamily: {
      sans: ["Roboto", "sans-serif"],
    },
    extend: {
      colors: {
        primary: "#001F34",
        secondary: '#3F6188',
        background: '#DBF2FF',
        accent: '#DEA01E',
        hover: '#182354',
        accentHover: '#dea01edd',
        Gray: "#181818",
        DarkGray: "#1e222b",
        DarkGrayHover: "#1b1f29",
        DarkSecondary: "#182230",
      }
    },
  },
  plugins: [
  ],
}
