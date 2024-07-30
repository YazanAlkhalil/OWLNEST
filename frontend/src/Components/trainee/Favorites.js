import React, { useState } from 'react'
import ProgressBar from "@ramonak/react-progress-bar";
import { FaStar } from "react-icons/fa";
import { useNavigate } from 'react-router-dom';
import useFetch from '../AuthComponents/UseFetch';


export default function Favorites({data,id}) {
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
    console.log(res);
  }
  return (
    <div className="">
    <img className="w-[330px] hover:cursor-pointer border  rounded" alt="error" 
    src={`http://127.0.0.1:8000/api${data?.image}`}  onClick={() => {navigate("/trainee/courses/id");}} />
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
    <FaStar className={`${fav ? "text-accent"  : "text-slate-500"} hover:cursor-pointer`} onClick={handleIconClick} />
    </div>

  </div>
  )
}
