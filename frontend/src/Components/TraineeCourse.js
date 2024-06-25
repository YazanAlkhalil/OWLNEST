import React from 'react'
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom'
import { clickCourse } from '../features/ClickCourse';

export default function TraineeCourse({image,name}) {
    const navigate = useNavigate();
    const dispatch = useDispatch();
    const handleClickCourse = () => {
      dispatch(clickCourse());
      navigate('id');
    }
  return (
    <div onClick={handleClickCourse} className='hover:cursor-pointer'>
      <img className='w-4/5 rounded' src={image} alt='error'/>
      <div className='text-xl bg-primary text-white w-4/5 mt-2 py-1 px-2 rounded'>{name}</div>
    </div>
  )
}
