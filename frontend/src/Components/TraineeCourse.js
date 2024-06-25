import React from 'react'
import { useNavigate } from 'react-router-dom'


export default function TraineeCourse({image,name}) {
    const navigate = useNavigate();
    const handleClickCourse = () => {
      navigate('id');
    }
  return (
    <div onClick={handleClickCourse} className='hover:cursor-pointer'>
      <img className='w-4/5 rounded' src={image} alt='error'/>
      <div className='text-xl bg-primary text-white w-4/5 mt-2 py-1 px-2 rounded'>{name}</div>
    </div>
  )
}
