import React from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import Content from '../Content';
import { useNavigate, useParams } from 'react-router-dom';

const lessons = [
  {
    id: 1,
    title: "Lesson 1",
    type: "video"
  },
  {
    id: 2,
    title: "Lesson 2",
    type: "exam"
  },
  {
    id: 3,
    title: "Lesson 3",
    type: "pdf"
  }
]
const lessons2 = [
  {
    id: 1,
    title: "Lesson 1",
    type: "pdf"
  },
  {
    id: 2,
    title: "Lesson 2",
    type: "video"
  },
  {
    id: 3,
    title: "Lesson 3",
    type: "pdf"
  }
]

export default function TraineeCourseDisplay() {
  const navigate = useNavigate();
  const {id} = useParams();
  console.log(id);
  const onGoBackClick = ()=>{
    navigate('/trainee/courses');
  }
  return (
    <div>
     <FontAwesomeIcon className="cursor-pointer text-2xl" icon={faArrowLeft} onClick={onGoBackClick} />
     <div className='p-5 font-black text-2xl'>
      Course Name : Complete React Course
     </div>
     <div className='px-7'>
      <Content unit={'Introduction'} lessons={lessons} />
      <Content unit={'Unit 1'} lessons={lessons} />
      <Content unit={'Unit 2'} lessons={lessons2} />
     </div>
    </div>
  )
}
