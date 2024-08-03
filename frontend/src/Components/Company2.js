import React from "react";
import { useNavigate } from "react-router-dom";

export default function Company({image,id,name}) {
  async function getRoles() {
    const res = await fetchData({ url: 'http://127.0.0.1:8000/api/company/' + companyId + '/roles/', method: 'get' });
    if (Array.isArray(res)) {
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

    const navigate = useNavigate();
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
