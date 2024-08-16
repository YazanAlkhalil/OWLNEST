import React, { useEffect, useRef, useState } from 'react'
import logo from "./../images/logo.png";
import image from "../images/simple-user-default-icon-free-png.webp";
import { CiSettings } from 'react-icons/ci';
import { LuLogOut } from 'react-icons/lu';
import { useDispatch } from 'react-redux';
import { logout } from '../features/Auth/LoginSlice';
import { useNavigate } from 'react-router-dom';
import { FaHouseMedicalCircleExclamation } from 'react-icons/fa6';

function Navbar2({name,image}) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [dropdown,setDropdown] = useState(false)
  const overlayRef = useRef(null);
  const toggleOverlay = () => {
    setDropdown(!dropdown);
  };
  const handleLogoutButton = () => {
    dispatch(logout());
    navigate('/');
}
 const handleCompanyClickButton = () => {
    navigate('/companyDetails',{replace: true})
 }
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
    <div className='flex justify-between items-center py-2 px-4 dark:bg-DarkGray bg-primary'>
  <img className='w-16 sm:w-20 mb-2 sm:mb-0' src={logo} alt="Logo" />
  <div className='flex items-center justify-end w-full sm:w-auto'>
    <div className='relative flex items-center'>
      <h3 className='pr-4 text-white'>{name}</h3>
      <img src={`http://127.0.0.1:8000/api${image}`} alt='error' onClick={toggleOverlay} className='h-12 hover:cursor-pointer rounded-full'></img>
      <div ref={overlayRef} className={`${dropdown ? "block" : "hidden"} dark:bg-DarkGray bg-white shadow-lg border-solid border border-slate-100 rounded w-48 absolute top-12 right-0 z-10`}>
        <div onClick={()=> navigate('/settings/general')} className='hover:bg-slate-200 dark:hover:bg-Gray dark:text-white px-4 py-2 hover:cursor-pointer rounded'>
          <CiSettings className='inline size-5 mr-2' />settings
        </div>
        <div onClick={handleLogoutButton} className='hover:bg-slate-200 dark:hover:bg-Gray dark:text-white px-4 py-2 hover:cursor-pointer rounded'>
          <LuLogOut className='inline size-5 mr-2' />logout
        </div>
        <div onClick={handleCompanyClickButton} className='hover:bg-slate-200 dark:hover:bg-Gray dark:text-white px-4 py-2 hover:cursor-pointer rounded'>
          <FaHouseMedicalCircleExclamation className='inline size-5 mr-2' />Create NEST
        </div>
      </div>
    </div>
  </div>
</div>
  )
}

export default Navbar2