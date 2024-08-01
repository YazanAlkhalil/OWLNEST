import React, { useEffect, useState } from 'react';
import logo from '../images/simple-user-default-icon-free-png.webp';
import useFetch from '../Components/AuthComponents/UseFetch';



export default function SettingsAccount() {
    const [photo, setPhoto] = useState(logo);
    const { fetchData } = useFetch();

    const handlePhotoChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = () => {
          setPhoto(reader.result);
        };
        reader.readAsDataURL(file);
      }
    };
    useEffect(()=>{
        async function getUserData (){
            const res = await fetchData({ url: 'http://127.0.0.1:8000/api/user/', method: 'get'});
            console.log(res);
        }
        getUserData();
    },[])
  
    const handleButtonClick = () => {
      document.getElementById('photo-input').click();
    };
  return (
    <>
      <div>
      <div>
        <h1>Edit Your Profile</h1>
        </div>
        <div className="relative inline-block">
      <img
        src={photo}
        alt="Profile Photo"
        className="w-24 h-24 rounded-full border border-white"
      />
      <input
        id="photo-input"
        type="file"
        accept="image/*"
        className="hidden"
        onChange={handlePhotoChange}
      />
      <button
        onClick={handleButtonClick}
        className="absolute bottom-0 right-0 bg-white p-1 rounded-full border border-gray-300"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          width="16"
          height="16"
          fill="currentColor"
          className="text-gray-600"
        >
          <path d="M0 0h24v24H0z" fill="none" />
          <path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zm2.92 1.92l.85-.85 2.67 2.67-.85.85H5.92zm3.3-3.3l2.67 2.67 8.5-8.5-2.67-2.67-8.5 8.5z" />
        </svg>
      </button>
    </div>
    <div>
        <h1>Username :</h1>
        <input type="text" name="username"
        className="w-full px-3 py-2 placeholder-gray-300 border border-gray-300
        rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-indgo-300 transition-colors duration-150" />
    </div>
    <div>
        <h1>Email :</h1>
        <input type="text" name="email"
        className="w-full px-3 py-2 placeholder-gray-300 border border-gray-300
        rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-ind
        go-300 transition-colors duration-150" />
    </div>
    <div>
        <h1>Phone :</h1>
        <input type="text" name="phone"
        className="w-full px-3 py-2 placeholder-gray-300 border border-gray-300
        rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-ind
        go-300 transition-colors duration-150" />
    </div>
    <div>
        <h1>Birthday :</h1>
        <input type="date" name="birthday"
        className="w-full px-3 py-2 placeholder-gray-300 border border-gray-300
        rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-ind
        go-300 transition-colors duration-150" />
    </div>
      </div> 
    </>
  )
}
