import React from "react";
import { useLocation, useNavigate } from "react-router-dom";
import useFetch from "./AuthComponents/UseFetch";

export default function Company({image,id,name}) {
  const {fetchData} = useFetch()
  const navigate = useNavigate();
  async function getRoles() {
    const res = await fetchData({ url: 'http://127.0.0.1:8000/api/company/' + id + '/roles/', method: 'get' });
    if (Array.isArray(res)) {
      const ownerIndex = res.findIndex(item => item === 'owner')
      if (ownerIndex != -1) {
        localStorage.setItem('isOwner', true)
        res[ownerIndex] = 'admin'
      }
      else{
        localStorage.setItem('isOwner', false)
      }   
      localStorage.setItem('roles', res)
      navigate(`/${res[0]}`)
      }
  }

    function handleCompanyClick() {
        getRoles()
        localStorage.setItem('companyId',id)
    }
    
  return (
      <div className="border-accent flex justify-center items-center border-4 rounded-md p-4 dark:bg-DarkGray dark:hover:bg-DarkGrayHover bg-primary hover:bg-hover cursor-pointer" onClick={handleCompanyClick}>
        <img
          className="w-1/2"
          src={`http://127.0.0.1:8000/api${image}`}
          alt="error"
        />   
      </div>
  );
}
