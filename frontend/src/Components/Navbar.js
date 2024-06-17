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
    <div className='tw-flex tw-justify-evenly tw-items-center tw-py-2 '>
      <div className='tw-flex tw-items-center tw-flex-grow tw-justify-evenly'>

        <a className={highlight == "trainee" ? "tw-text-accent": ""} href="#">Trainee</a>
        <a className={highlight == "trainer" ? "tw-text-accent": ""} href="#">Instructor</a>
        <a className={highlight == "admin" ? "tw-text-accent": ""} href="#">Admin</a>
      </div>
      <div className='tw-flex tw-items-center tw-flex-grow tw-justify-end '>

        <IoIosNotifications className='tw-size-8 tw-hover:cursor-pointer'/>
        <div className='tw-relative tw-flex tw-items-center tw-px-8'>
          <h3 className='tw-pr-4'>username</h3>
          <img src={image} onClick={toggleOverlay} className='tw-h-12 tw-hover:cursor-pointer tw-rounded-full'></img>
        <div ref={overlayRef} className={`${dropdown? "tw-block" :"tw-hidden"} tw-bg-slate-300 tw-rounded  tw-absolute tw-top-12 tw-right-14`}>
          <div className='tw-hover:bg-slate-500 tw-px-4 py-2 tw-hover:cursor-pointer tw-rounded tw-hover:text-white'>settings</div>
          <div className='tw-hover:bg-slate-500 tw-px-4 py-2 tw-hover:cursor-pointer tw-rounded tw-hover:text-white'>logout</div>
        </div>
        </div>
      </div>
    </div>
  )
}

export default NavBar
