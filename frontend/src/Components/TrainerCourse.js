import React from 'react'
import { useNavigate } from 'react-router-dom'
import def from '../images/default-course-thumbnail.png'
function TrainerCourse({name,image,id}) {
    const navigate = useNavigate()
    
  return (
    <div onClick={()=> {navigate(`${id}`); localStorage.setItem('courseName',name)}} className='hover:cursor-pointer'>
      <img className='border border-black shadow-lg w-4/5 rounded' src={image ? image : def}/>
      <div className='text-xl dark:bg-DarkGray bg-primary text-white w-4/5 mt-2 py-1 px-2 rounded'>{name}</div>
    </div>
  )
}

export default TrainerCourse
