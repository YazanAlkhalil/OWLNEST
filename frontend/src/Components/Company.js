import React from "react";
import backGround from './../images/multimedia-courses-scope-and-career 1.png';
import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { clickCompany } from "../features/ClickCompany";
import logo from './../images/logo.png';

export default function Company() {
    const value = useSelector(state => state.clickCompany.value);
    const dispatch = useDispatch();
    const navigate = useNavigate()
    function handleCompanyClick() {
        dispatch(clickCompany(false));
        navigate('/trainee',{replace: true});
        
    }
  return (
    <>
      <div class="relative w-1/4 rounded-full cursor-pointer" onClick={handleCompanyClick}>
        <img
          className="h-50 w-full object-cover rounded-full"
          src={logo}
          alt="error"
        />
        <div class="absolute inset-0 bg-gray-700 opacity-60 rounded-full"></div>
        <div class="absolute inset-0 flex items-center justify-center">
          <h2 class="text-white text-3xl font-bold">Syriatel</h2>
        </div>
      </div>
    </>
  );
}
