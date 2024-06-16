import React from 'react'

function NavButton({name,highlight,handleClick}) {
  return (
    <div>
      <button onClick={handleClick} className={`${highlight? "bg-accent": "bg-primary hover:bg-hover"} text-white px-4 py-2 rounded `}>
        {name}
      </button>
    </div>
  )
}

export default NavButton
