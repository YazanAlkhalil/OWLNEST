import React from 'react'
import Sidebar from './Sidebar';
import NavBar from './Navbar';
import { Outlet, useNavigate } from 'react-router-dom';
import { IoArrowBack } from 'react-icons/io5';

function SettingsLayout() {
    const roles = localStorage.getItem('roles');
    console.log(roles);
    const navigate = useNavigate()
    function handleGoBack(){
        if(roles.includes('admin'))
            navigate('/admin')
        else if(roles.includes('trainee'))
            navigate('/trainee')
        else 
            navigate('/trainer')
    }
    return (
        <div className="grid grid-cols-6 h-screen">
            <Sidebar links={[
                { name: "General", url: "/settings/general" },
                { name: "Account", url: "/settings/account" },
                { name: "Company", url: "/settings/company" },
            ]} />
            <div className="dark:bg-Gray dark:text-white h-screen col-span-5 overflow-auto flex flex-col grow-[24]">
                <NavBar />
                <main className="flex-1 p-8 overflow-auto">
                    <IoArrowBack onClick={handleGoBack} className='size-6 mb-10 hover:cursor-pointer' />
                    <Outlet />
                </main>
            </div>
        </div>
    );
}

export default SettingsLayout
