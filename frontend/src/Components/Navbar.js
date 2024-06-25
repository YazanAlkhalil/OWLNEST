import React, { useEffect, useRef, useState } from "react";
import image from "../images/40npx.png";
import { IoIosNotifications } from "react-icons/io";
import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import logo from "./../images/logo.png";
import { CiSettings } from "react-icons/ci";
import { FaExchangeAlt } from "react-icons/fa";
import { LuLogOut } from "react-icons/lu";
import { clickChnageCompany, clickCompany } from "../features/ClickCompany";
import Badge from '@mui/material/Badge';

function NavBar({ highlight }) {
  const navProp = useSelector((state) => state.clickCompany.value);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [dropdown, setDropdown] = useState(false);
  const overlayRef = useRef(null);
  const toggleOverlay = () => {
    setDropdown(!dropdown);
  };
  const handleClickOutside = (event) => {
    if (overlayRef.current && !overlayRef.current.contains(event.target)) {
      setDropdown(false);
    }
  };
  const handleChangeCompanyClick = () => {
    dispatch(clickChnageCompany());
    navigate('/company',{replace: true});
  }
  useEffect(() => {
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, []);

  return (
    <div
      className={
        navProp
          ? "flex justify-evenly items-center py-2 "
          : "flex justify-evenly items-center bg-slate-500 p-2"
      }>
      <div
        className={
          navProp ? "flex items-center flex-grow justify-evenly" : "ml-7"
        }>
        {navProp ? (
          <>
            <NavLink
              className={highlight === "trainee" ? "text-accent" : ""}
              to="/trainee">
              Trainee
            </NavLink>
            <NavLink
              className={highlight === "trainer" ? "text-accent" : ""}
              to="/trainer">
              Instructor
            </NavLink>
            <NavLink
              className={highlight === "admin" ? "text-accent" : ""}
              to="/admin">
              Admin
            </NavLink>
          </>
        ) : (
          <img src={logo} alt="error" className="w-[100px] h-[100px]" />
        )}
      </div>
      <div className="flex items-center flex-grow justify-end ">
        {navProp ? (
          <Badge badgeContent={4} color="error">
          <IoIosNotifications className="size-8 hover:cursor-pointer" />
          </Badge>
        ) : (
          <></>
        )}
        <div className="relative flex items-center px-8">
          <h3 className="pr-4">username</h3>
          <img
            src={image}
            alt="error"
            onClick={toggleOverlay}
            className="h-12 hover:cursor-pointer rounded-full"></img>
          <div ref={overlayRef} className={`${dropdown ? "block" :"hidden"} bg-white shadow-lg border-solid border border-slate-100 rounded w-48  absolute z-50 top-12 right-14`}>
          <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded'><CiSettings className='inline size-5 mr-2'/>settings</div>
          <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded' onClick={handleChangeCompanyClick}><FaExchangeAlt className='inline size-5 mr-2'/>change company</div>
          <div className='hover:bg-slate-200 px-4 py-2 hover:cursor-pointer rounded'><LuLogOut className='inline size-5 mr-2'/>logout</div>
        </div>
        </div>
      </div>
    </div>
  );
}

export default NavBar;
