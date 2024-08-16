import React from "react";
import Sidebar from "./Sidebar";
import NavBar from "./Navbar";
import { Outlet, useNavigate } from "react-router-dom";
import { IoArrowBack } from "react-icons/io5";

function SettingsLayout() {
  const roles = localStorage.getItem("roles");
  let isOwner = localStorage.getItem("isOwner");
  if(isOwner === 'true'){
    isOwner = true;
  }else {
    isOwner = false
  }
  console.log(roles);
  console.log(isOwner);
  const navigate = useNavigate();
  function handleGoBack() {
    if (roles.includes("admin")) navigate("/admin");
    else if (roles.includes("trainee")) navigate("/trainee");
    else navigate("/trainer");
  }
  return (
    <div className="grid grid-cols-6 h-screen">
      {isOwner ? (
        <Sidebar
          links={[
            { name: "Theme", url: "/settings/general" },
            { name: "Account", url: "/settings/account" },
            { name: "Company", url: "/settings/company" },
          ]}
        />
      ) : (
        <Sidebar
          links={[
            { name: "Theme", url: "/settings/general" },
            { name: "Account", url: "/settings/account" },
          ]}
        />
      )}

      <div className="dark:bg-Gray dark:text-white h-screen col-span-5 overflow-auto flex flex-col grow-[24]">
        <NavBar />
        <main className="flex-1 p-8 overflow-auto">
          <IoArrowBack
            onClick={handleGoBack}
            className="size-6 mb-10 hover:cursor-pointer"
          />
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default SettingsLayout;
