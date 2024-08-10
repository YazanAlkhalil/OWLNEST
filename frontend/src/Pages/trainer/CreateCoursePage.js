import React from 'react'
import NavButton from '../../Components/NavButton'
import CourseEdit from '../../Components/CourseEdit'
import CourseReports from '../../Components/CourseReports'
import CourseTrainees from '../../Components/CourseTrainees'
import { useState } from 'react'
import { BiArrowBack } from 'react-icons/bi'
import { useNavigate } from 'react-router-dom'

function CreateCoursePage({ inprogress }) {
  const [content, setContent] = useState('edit')
  const navigate = useNavigate()

  return (
    <>
      <div className='flex gap-6 items-start'>
        <BiArrowBack className='size-7 hover:cursor-pointer ' onClick={() => {
          if (inprogress)
            navigate('/trainer/inprogress')
          else
            navigate('/trainer')
        }} />
        <NavButton name={'Edit'} highlight={content === 'edit'} handleClick={() => setContent('edit')} />
        <NavButton name={'Reports'} highlight={content === 'reports'} handleClick={() => setContent('reports')} />
        <NavButton name={'Trainees'} highlight={content === 'trainees'} handleClick={() => setContent('trainees')} />
      </div>
      <div className='pt-10'>
        {content === "edit" && <CourseEdit inprogress={inprogress} />}
        {content === "reports" && <CourseReports admin={true} />}
        {content === "trainees" && <CourseTrainees />}
      </div>
    </>

  )
}

export default CreateCoursePage
