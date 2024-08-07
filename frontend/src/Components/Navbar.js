import React, { useEffect, useRef, useState } from "react";
import image from "../images/simple-user-default-icon-free-png.webp";
import { IoIosNotifications } from "react-icons/io";
import { NavLink, Navigate, useLocation, useNavigate } from "react-router-dom";
import { CiSettings } from "react-icons/ci";
import { FaExchangeAlt } from "react-icons/fa";
import { LuLogOut } from "react-icons/lu";
import Badge from '@mui/material/Badge';
import { useDispatch } from "react-redux";
import { logout } from "../features/Auth/LoginSlice";
import UseFetch from "./AuthComponents/UseFetch";
import NotificationList from "./NotificationsList";



function NavBar({ highlight }) {
  const navigate = useNavigate();
  const dispatch = useDispatch()
  const { fetchData, resData } = UseFetch()
  const [dropdown, setDropdown] = useState(false);
  const [notifyDropDown, setNotifyDropDown] = useState(false);
  const [notificationsList, setNotificationsList] = useState([]);
  const overlayRef = useRef(null);
  const companyId = localStorage.getItem('companyId');
  const username = localStorage.getItem('username');
  const [notifications, setNotifications] = useState(0)
  const audioRef = useRef(null);
  const lastNotificationRef = localStorage.getItem('lastNotificationRef');
  const roles = localStorage.getItem('roles');


  useEffect(() => {
    const ws = new WebSocket('ws://127.0.0.1:8000/ws/company/' + companyId + '/notification/')
    ws.onopen = (event) => {
      console.log('WebSocket connected');
    };
    ws.onmessage = (event) => {
      let message = JSON.parse(event.data);
      message = message.message.toString()
      message = message[message.length - 1]
      if (message === "0") {
        message = null;
      } else {
        console.log(message);
        console.log(lastNotificationRef);
        if (lastNotificationRef != message) {
          if (!audioRef.current) {
            audioRef.current = new Audio('/cute_notification.mp3');
          }
          audioRef.current.play().catch(error => console.log('Audio play failed:', error));
          localStorage.setItem('lastNotificationRef', message)
        }
      }
      setNotifications(message)
    };
    ws.onclose = (event) => {
      console.log('WebSocket disconnected');
    };
    return () => {
      ws.close();
    };

  }, [])

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
  const handleSettingsClick = () => {
    navigate('/settings/general');
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



  async function toggleNotifications() {
    if (notifyDropDown)
      setNotifyDropDown(false)
    else {
      const data = await fetchData({ url: "http://127.0.0.1:8000/api/user/company/" + companyId + "/notifications" })
      if (data)
        data.reverse()
      setNotificationsList(data)
      setNotifications(null)
      setNotifyDropDown(true)
    }
  }
  return (
    <div
      className={"flex justify-evenly items-center py-2 pt-4 "
      }>


      {roles && roles.includes(',')
        &&
        <div
          className={
            "flex items-center flex-grow justify-evenly"
          }>
          <>
            {roles.includes('trainee')
              && <NavLink
                className={highlight === "trainee" ? "text-accent" : ""}
                to="/trainee">
                Trainee
              </NavLink>}
            {roles.includes('trainer')
              && <NavLink
                className={highlight === "trainer" ? "text-accent" : ""}
                to="/trainer">
                Instructor
              </NavLink>}
            {(roles.includes("admin") || roles.includes("owner")) && <NavLink
              className={highlight === "admin" ? "text-accent" : ""}
              to="/admin">
              Admin
            </NavLink>

            }
          </>
        </div>}


      <div className="flex items-center flex-grow justify-end ">
        <Badge onClick={toggleNotifications} badgeContent={notifications} color="error">
          <IoIosNotifications className="size-8 hover:cursor-pointer" />
          {
            notifyDropDown && <NotificationList notifications={notificationsList} />
          }
        </Badge>
        <div className="relative flex items-center px-8">
          <h3 className="pr-4">{username}</h3>
          <img
            src={image}
            alt="error"
            onClick={toggleOverlay}
            className="h-10 w-10 hover:cursor-pointer rounded-full"></img>
          <div ref={overlayRef} className={`${dropdown ? "block" : "hidden"} bg-white dark:bg-DarkGray shadow-lg border-solid border border-slate-100 rounded w-48  absolute z-50 top-12 right-14`}>
            <div className='hover:bg-slate-200 dark:hover:bg-Gray px-4 py-2 hover:cursor-pointer rounded' onClick={handleSettingsClick}><CiSettings className='inline size-5 mr-2' />settings</div>
            <div className='hover:bg-slate-200 px-4 dark:hover:bg-Gray py-2 hover:cursor-pointer rounded' onClick={handleChangeCompanyClick}><FaExchangeAlt className='inline size-5 mr-2' />change company</div>
            <div className='hover:bg-slate-200 px-4 dark:hover:bg-Gray py-2 hover:cursor-pointer rounded' onClick={handleLogoutButton}><LuLogOut className='inline size-5 mr-2' />logout</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default NavBar;
