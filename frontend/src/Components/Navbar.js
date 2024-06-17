import React, { useEffect, useRef, useState } from 'react'
import image from '../images/40npx.png'
import { IoIosNotifications } from "react-icons/io";



function NavBar({highlight}) {
  const [dropdown,setDropdown] = useState(false)
  const overlayRef = useRef(null);
  const toggleOverlay = () => {
    setDropdown(!dropdown);
  };
  const handleClickOutside = (event) => {
    if (overlayRef.current && !overlayRef.current.contains(event.target)) {
      setDropdown(false);
    }
  };
  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  return (
    <div className='flex justify-evenly items-center py-2 '>
      <div className='flex items-center flex-grow justify-evenly'>

        <a className={highlight == "trainee" ? "text-accent": ""} href="#">Trainee</a>
        <a className={highlight == "trainer" ? "text-accent": ""} href="#">Instructor</a>
        <a className={highlight == "admin" ? "text-accent": ""} href="#">Admin</a>
      </div>
      <div className='flex items-center flex-grow justify-end '>

        <IoIosNotifications className='size-8 hover:cursor-pointer'/>
        <div className='relative flex items-center px-8'>
          <h3 className='pr-4'>username</h3>
          <img src={image} onClick={toggleOverlay} className='h-12 hover:cursor-pointer rounded-full'></img>
        <div ref={overlayRef} className={`${dropdown? "block" :"hidden"} bg-slate-300 rounded  absolute top-12 right-14`}>
          <div className='hover:bg-slate-500 px-4 py-2 hover:cursor-pointer rounded hover:text-white'>settings</div>
          <div className='hover:bg-slate-500 px-4 py-2 hover:cursor-pointer rounded hover:text-white'>logout</div>
        </div>
        </div>
      </div>
    </div>
  )
}

export default NavBar
