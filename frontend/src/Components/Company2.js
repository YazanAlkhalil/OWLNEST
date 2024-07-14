import React from "react";
import { useNavigate } from "react-router-dom";

export default function Company({image,id}) {
    const navigate = useNavigate()
    function handleCompanyClick() {
        localStorage.setItem('companyId',id)
        navigate('/trainee');
    }
  return (
      <div className="border-accent flex justify-center items-center border-4 rounded-md p-4 bg-primary hover:bg-hover cursor-pointer" onClick={handleCompanyClick}>
        <img
          className="w-1/2"
          src={image}
          alt="error"
        />        
      </div>
  );
}
