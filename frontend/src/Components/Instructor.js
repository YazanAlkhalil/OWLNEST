import React from 'react';
import logo from './../images/simple-user-default-icon-free-png.webp';

export default function Instructor({name}) {
  return (
    <div className='flex my-4 mx-2'>
        <img src={logo} alt='error' className='w-[70px] h-[70px] ' />
        <h1 className='py-5 text-xl font-semibold'>{name}</h1>
    </div>
  )
}
