import React from "react";
import { useNavigate } from "react-router-dom";
import logo from './../images/logo.png';

export default function Company() {
    const navigate = useNavigate()
    function handleCompanyClick() {
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
