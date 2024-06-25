import React from 'react';
import logo from './../images/user-profile-icon-flat-style-member-avatar-vector-illustration-isolated-background-human-permission-sign-business-concept_157943-15752.avif';
import { FaReply } from "react-icons/fa6";
import { BiLike } from "react-icons/bi";
import { BiDislike } from "react-icons/bi";

export default function Comment() {
  return (
    <>
      <div className='flex justify-between'>
        <div className='flex'>
            <img src={logo} alt='error' className='w-[50px] h-[50px] ' />
            <div>
              <h4>Username</h4>
              <p>Comment text</p>
              <div className='flex'>
                <p>replies</p>
                <FaReply />
              </div>
            </div>
        </div>
        <div>
            <div className='flex'>
            <div className='border-r-2 flex border-r-stone-950 px-10 py-1'>
            <BiLike />
            <p>4</p>
            </div>
            <div className='px-10 py-1 flex'>
            <BiDislike />
            <p>1</p>
            </div>
            </div>
        </div>
      </div>
    </>
  )
}
