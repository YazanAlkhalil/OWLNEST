import React, { useEffect, useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import { Button } from "@mui/material";
import { IoCheckmarkDoneSharp } from "react-icons/io5";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import useFetch from "../AuthComponents/UseFetch";

export default function TraineeVideoLesson() {
  const navigate = useNavigate();
  const { state } = useLocation();
  const[loading, setLoading] = useState(true);
  const lessonId = localStorage.getItem('lessonId');
  const { fetchData, resData } = useFetch();
  const {id} = useParams()
  const onGoBackClick = () => {
    navigate(`/trainee/courses/${id}/content`);
  };

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/ws/course/1/content/1");

 
    socket.onclose = function (e) {
      console.error("WebSocket closed unexpectedly");
    };

    return () => {
      socket.close();
    };
  }, []);
  useEffect(()=>{
    console.log(state);
    const getVideo = async ()=>{
      const res = await fetchData({
        url:
          "http://127.0.0.1:8000/api/trainee/content/"+state,
        method: "get",
      });
      console.log(res);
      if(res){
        setLoading(false);
      }
    }
    getVideo()
  },[])
  console.log(lessonId);
  async function mark(){
    

    const res = await fetchData({url:`/course/${id}/mark-content/${lessonId}`,method:"POST"})
    console.log(res.status);
    
    if(res.status === "passed"){
      navigate(`/trainee/courses/${id}/content/Congratulations`)
    }else{
      onGoBackClick()
    }

  }

  return (
    <div>
      <FontAwesomeIcon
        className="cursor-pointer text-2xl"
        icon={faArrowLeft}
        onClick={onGoBackClick}
      />
      <div className="mt-10">
        {!loading && <video className="h-[70%] mx-auto w-[70%] rounded-lg" controls  autoPlay>
          <source
            src={resData?.file}
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>}
      </div>
      <div className="w-[70%] mt-10 mx-auto">
        <h1 className="text-2xl font-semibold">Description : </h1>
        <p className="text-md px-5 py-10">
          {resData?.description}
        </p>
      </div>
      <div className="w-[70%] mx-auto flex justify-end">
        <button onClick={mark} className="btn-inner">Mark as completed</button>
      </div>
    </div>
  );
}
