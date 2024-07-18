import React, { useEffect, useRef, useState } from "react";
import image from "../images/40npx.png";
import { IoIosNotifications } from "react-icons/io";
import { NavLink, Navigate, useLocation, useNavigate } from "react-router-dom";
import { CiSettings } from "react-icons/ci";
import { FaExchangeAlt } from "react-icons/fa";
import { LuLogOut } from "react-icons/lu";
import Badge from '@mui/material/Badge';
import { useDispatch } from "react-redux";
import { logout } from "../features/Auth/LoginSlice";
import UseFetch from "./AuthComponents/UseFetch";



function NavBar({ highlight }) {
  const navigate = useNavigate();
  const dispatch = useDispatch()
  const location = useLocation();
  const { fetchData, resData } = UseFetch()
  const [dropdown, setDropdown] = useState(false);
  const overlayRef = useRef(null);
  const companyId = localStorage.getItem('companyId');
  useEffect(() => {
    async function getRoles() {
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/company/'+companyId+'/roles/', method: 'get' });
      if (Array.isArray(res) && res.length === 1) {
        let role = res[0] === 'owner' ? 'admin' : res[0];
        let targetPath = `/${role}`;
        
        if (!location.pathname.startsWith(targetPath)) {
          navigate(targetPath);
        }
      }
    }
    getRoles();
  }, [navigate, location.pathname]);




  const toggleOverlay = () => {
    setDropdown(!dropdown);
  };
  const handleClickOutside = (event) => {
    if (overlayRef.current && !overlayRef.current.contains(event.target)) {
      setDropdown(false);
    }
  };
  const handleLogoutButton = () => {
    dispatch(logout());
    navigate('/');
  }
  const handleChangeCompanyClick = () => {
    navigate('/company', { replace: true });
  }
  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <div
      className={"flex justify-evenly items-center py-2 "
      }>


      {Array.isArray(resData) && resData.length > 1
        &&

        <div
          className={
            "flex items-center flex-grow justify-evenly"
          }>
          <>
            {Array.isArray(resData) && resData.includes('trainee')
              && <NavLink
                className={highlight === "trainee" ? "text-accent" : ""}
                to="/trainee">
                Trainee
              </NavLink>}
            {Array.isArray(resData) && resData.includes('trainer')
              && <NavLink
                className={highlight === "trainer" ? "text-accent" : ""}
                to="/trainer">
                Instructor
              </NavLink>}
            {Array.isArray(resData) && (resData.includes("admin") || resData.includes("owner")) && <NavLink
              className={highlight === "admin" ? "text-accent" : ""}
              to="/admin">
              Admin
            </NavLink>

            }
          </>
        </div>}


      <div className="flex items-center flex-grow justify-end ">
        <Badge badgeContent={4} color="error">
          <IoIosNotifications className="size-8 hover:cursor-pointer" />
        </Badge>
        <div className="relative flex items-center px-8">
          <h3 className="pr-4">username</h3>
          <img
            src={image}
            alt="error"
            onClick={toggleOverlay}
            className="h-12 hover:cursor-pointer rounded-full"></img>
          <div ref={overlayRef} className={`${dropdown ? "block" : "hidden"} bg-white shadow-lg border-solid border border-slate-100 rounded w-48  absolute z-50 top-12 right-14`}>
            <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded'><CiSettings className='inline size-5 mr-2' />settings</div>
            <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded' onClick={handleChangeCompanyClick}><FaExchangeAlt className='inline size-5 mr-2' />change company</div>
            <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded' onClick={handleLogoutButton}><LuLogOut className='inline size-5 mr-2' />logout</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NavBar;
