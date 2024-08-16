import React, { useState } from 'react'
import ProgressBar from "@ramonak/react-progress-bar";
import { FaStar } from "react-icons/fa";
import { useNavigate } from 'react-router-dom';
import { FaHeart } from "react-icons/fa";

import useFetch from '../AuthComponents/UseFetch';


export default function Favorites({data,id,getFavorits}) {
    const navigate = useNavigate();
    const [fav,setFav] = useState(true);
    const { fetchData , resData } = useFetch();
    const companyID = localStorage.getItem('companyId');


    async function handleIconClick(){
      const data = {
        course : id
      }
    setFav(false);
    const res = await fetchData({url: 'http://127.0.0.1:8000/api/trainee/company/'+companyID+'/favorites',method : 'delete',data: data } )
    getFavorits()
    console.log(res);
  }
  return (
    <div className="">
    <img className="w-[330px] h-44 hover:cursor-pointer border  rounded" alt="error" 
    src={`${data?.image}`}  onClick={() => {navigate("/trainee/courses/id");}} />
    <ProgressBar
    completed={data?.progress}
    labelColor="#FFFFFF"
    bgColor="#001f34"
    transitionDuration="2s"
    transitionTimingFunction="linear"
    animateOnRender
    className="mt-3"
  />
    <div className="text-xl font-semibold w-[330px] mt-2 py-1 px-2">
      {data?.course}
    </div>
    <div className="px-2 py-1 text-xl flex justify-between"> 
    <h1 className="font-semibold">By {data?.trainer}</h1>
    <FaHeart className={`${"text-red-600"} hover:cursor-pointer`} onClick={handleIconClick} />
    </div>

  </div>
  )
}