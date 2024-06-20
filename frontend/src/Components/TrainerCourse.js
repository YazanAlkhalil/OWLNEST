import React from 'react'
import { useNavigate } from 'react-router-dom'
function TrainerCourse({name,image}) {
    const navigate = useNavigate()
  return (
    <div onClick={()=> {navigate('id')}} className='hover:cursor-pointer'>
      <img className='w-4/5 rounded' src={image}/>
      <div className='text-xl bg-primary text-white w-4/5 mt-2 py-1 px-2 rounded'>{name}</div>
    </div>
  )
}

export default TrainerCourse
