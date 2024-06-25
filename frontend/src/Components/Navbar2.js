import React, { useEffect, useRef, useState } from 'react'
import logo from "./../images/logo.png";
import image from "../images/40npx.png";
import { CiSettings } from 'react-icons/ci';
import { LuLogOut } from 'react-icons/lu';

function Navbar2() {
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
    <div className='flex justify-evenly items-center py-2 bg-primary'>
      <img className='w-20 ml-8' src={logo}/>
      <div className='flex items-center flex-grow justify-end '>

        <div className='relative flex items-center px-8'>
          <h3 className='pr-4 text-white'>username</h3>
          <img src={image} onClick={toggleOverlay} className='h-12 hover:cursor-pointer rounded-full'></img>
        <div ref={overlayRef} className={`${dropdown? "block" :"hidden"} bg-white shadow-lg border-solid border border-slate-100 rounded w-48  absolute top-12 right-14`}>
          <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded'><CiSettings className='inline size-5 mr-2'/>settings</div>
          <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded'><LuLogOut className='inline size-5 mr-2'/>logout</div>
        </div>
        </div>
      </div>
    </div>
  )
}

export default Navbar2
