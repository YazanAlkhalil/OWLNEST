import React, { useEffect, useState } from "react";
import Favorites from "./Favorites";
import useFetch from "../AuthComponents/UseFetch";


export default function TraineeFavorites() {

  const { fetchData , resData } = useFetch();
  const companyID = localStorage.getItem('companyId');

  useEffect(()=>{
      const getFavorits = async () => {
        const res = await fetchData({url: 'http://127.0.0.1:8000/api/trainee/company/'+companyID+'/favorites', method: 'get'}) 
        console.log(res);
      }
        getFavorits();
  },[])

  return (
    <div className="flex flex-wrap gap-3">
        {resData?.map((item,index)=>{
          return <Favorites key={index} id={index+1} data={item} />
        })}
    </div>
  );
}
