import React, { useEffect, useState } from 'react'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { useNavigate, useParams } from 'react-router-dom';
import useFetch from '../AuthComponents/UseFetch';
import Content from '../Content';


export default function TraineeCourseDisplay() {
  const { fetchData ,resData } = useFetch();
  const navigate = useNavigate();
  const [data,setData]  = useState({units:[]});
  const {id} = useParams();
  console.log(id);
  const onGoBackClick = ()=>{
    navigate('/trainee/courses');
  }
  useEffect(()=>{
    const getContent = async () =>{
      const res = await fetchData({
        url:
          "http://127.0.0.1:8000/api/trainee/courses/"+ id,
        method: "get",
      });
      console.log(res,"res");
      setData(res);
      
      
    }
    getContent();
  },[])
  console.log(data,"data");
  
  return (
    <div>
     <FontAwesomeIcon className="cursor-pointer text-2xl" icon={faArrowLeft} onClick={onGoBackClick} />
     <div className='p-5 font-black text-2xl'>
      Course Name : {data?.name}
     </div>
     <div className='px-7'>
      {data?.units.map((content)=>{
        return <Content key={content.id} data={content} />
       })} 
     </div>
    </div>
  )
}
