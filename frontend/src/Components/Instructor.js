import React from 'react';
import logo from './../images/simple-user-default-icon-free-png.webp';

export default function Instructor({name,image}) {
  console.log(image,"image");
  return (
    <div className='flex gap-4 my-4 mx-2'>
        <img src={image ? image : logo} alt='error' className='w-[70px] h-[70px] ' />
        <h1 className='py-5 text-xl font-semibold'>{name}</h1>
    </div>
  )
}
