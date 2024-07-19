import React from 'react'

function NotFoundPage() {
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-Gray flex flex-col justify-center items-center">
    <div className="text-center">
      <h1 className="text-9xl font-bold text-gray-200">404</h1>
      <h2 className="text-6xl font-medium py-8 text-gray-300">Oops! Page not found</h2>
      <p className="text-2xl pb-8 px-12 font-medium text-gray-400">
        The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.
      </p>
      <a
        href="/company"
        className="bg-hover dark:bg-DarkGray dark:hover:bg-DarkGrayHover hover:bg-primary text-white font-bold py-4 px-6 rounded-full text-xl transition duration-300 ease-in-out transform hover:scale-105"
      >
        Go Home
      </a>
    </div>
  </div>
  )
}

export default NotFoundPage
