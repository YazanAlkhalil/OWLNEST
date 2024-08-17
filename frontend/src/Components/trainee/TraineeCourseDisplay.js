import React, { useEffect, useState } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { useNavigate, useParams } from 'react-router-dom';
import useFetch from '../AuthComponents/UseFetch';
import Content from '../Content';
import { useDispatch } from 'react-redux';
import ChatComponent from './chatComponent';
import { toggleChat } from '../../features/chatSlice';


export default function TraineeCourseDisplay() {
  const dispatch = useDispatch()
  const { fetchData, resData } = useFetch();
  const navigate = useNavigate();
  const [data, setData] = useState({ units: [] });
  const { id } = useParams();
  console.log(id);
  const onGoBackClick = () => {
    navigate('/trainee/courses');
  }
  useEffect(() => {
    const getContent = async () => {
      const res = await fetchData({
        url:
          "http://127.0.0.1:8000/api/trainee/courses/" + id,
        method: "get",
      });
      console.log(res, "res");
      setData(res);


    }
    getContent();
  }, [])
  console.log(data, "data");

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-4xl mx-auto">
        <button 
          onClick={onGoBackClick}
          className="mb-6 flex items-center text-blue-600 hover:text-blue-800 transition-colors duration-200"
        >
          <FontAwesomeIcon icon={faArrowLeft} className="mr-2" />
          <span>Back to Courses</span>
        </button>
        
        <h1 className='text-4xl font-bold  mb-8'>
          {data?.name}
        </h1>
        
        <div className='space-y-8'>
          {data?.units.map((content) => (
            <Content key={content.id} id={id} data={content} />
          ))}
        </div>
      </div>
    </div>
  )
}
