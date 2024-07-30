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
  const location = useLocation();
  const { fetchData, resData } = UseFetch()
  const [dropdown, setDropdown] = useState(false);
  const [notifyDropDown, setNotifyDropDown] = useState(false);
  const [notificationsList, setNotificationsList] = useState([]);
  const overlayRef = useRef(null);
  const companyId = localStorage.getItem('companyId');
  const username = localStorage.getItem('username');
  const [notifications, setNotifications] = useState(0)
  useEffect(() => {
    const ws = new WebSocket('ws://127.0.0.1:8000/ws/company/' + companyId + '/notification/')
    ws.onopen = (event) => {
      console.log('WebSocket connected');
    };
    ws.onmessage = (event) => {
      let message = JSON.parse(event.data);
      message = message.message.toString()
      message = message[message.length - 1]
      if (message == "0")
        message = null
      else {
        const audio = new Audio('/cute_notification.mp3');
        audio.play();
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






  useEffect(() => {
    async function getRoles() {
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/company/' + companyId + '/roles/', method: 'get' });
      if (Array.isArray(res)) {
        console.log(res, "res");
        const ownerIndex = res.findIndex(item => item === 'owner')
        if (ownerIndex != -1) {
          localStorage.setItem('isOwner', true)
          res[ownerIndex] = 'admin'
        }
        else{
          localStorage.setItem('isOwner', false)
        }
        if (res.length === 1) {
          let targetPath = `/${res[0]}`;
          if (!location.pathname.startsWith(targetPath) && !location.pathname.startsWith('/settings')) {
            navigate(targetPath);
          }
        }
        localStorage.setItem('roles', res)
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
