import React from 'react'

import logo from './../images/user-profile-icon-flat-style-member-avatar-vector-illustration-isolated-background-human-permission-sign-business-concept_157943-15752.avif';
import { FaReply } from "react-icons/fa6";
import { BiLike } from "react-icons/bi";
import { BiDislike } from "react-icons/bi";


export default function Reply({name,text}) {
  return (
    <div>
     <div className='flex justify-between w-3/4 mx-auto px-6 py-5 '>
        <div className='flex'>
            <img src={logo} alt='error' className='w-[90px] h-[90px] ' />
            <div className='ml-3 my-4'>
              <h4 className='text-xl font-black'>{name}</h4>
              <p className='text-xl font-semibold'>{text}</p>
            </div>
        </div>
        <div>
            <div className='flex p-4'>
            <div className='border-r-2 flex border-r-stone-950 px-10 py-1 cursor-pointer'>
            <BiLike size={'30'} />
            <p className='ml-2 text-xl font-semibold'>4</p>
            </div>
            <div className='px-10 py-1 flex cursor-pointer'>
            <BiDislike size={'30'} />
            <p className='ml-2 text-xl font-semibold'>1</p>
            </div>
            </div>
        </div>
      </div>
    </div>
  )
}
