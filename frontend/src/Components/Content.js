import React from "react";
import { FaPlay, FaRegFilePdf } from "react-icons/fa";
import { PiExam } from "react-icons/pi";
import { useNavigate } from "react-router-dom";

function getIcon(icon) {
  if (icon === "video") return <FaPlay />;
  else if (icon === "pdf") return <FaRegFilePdf />;
  else return <PiExam />;
}


export default function Content({ data }) {
  const navigate = useNavigate();


  function handleClick(les) {
    localStorage.setItem("lessonId", les.id);
    if (les.type === 'video') {
      navigate('video', { state: les.id })
    }
    else if (les.type === 'pdf') {
      navigate('pdf', { state: les.id })
    }
    else
      navigate('quiz', { state: les.id })
  
  }

  
  return (
    <div className="m-3 ">
      <div className="flex justify-between px-2">
        <h1 className={`mb-4 font-semibold text-xl`}>{data.title} : </h1>
        {data?.is_completed ? <h1 className="text-green-500 text-semibold text-2xl">✔</h1> : ''}
      </div>
      {data.contents.map((les) => {
        return (
          <div
            key={les.id}
            className="flex dark:bg-DarkSecondary justify-between bg-gray-300 px-6 py-3 mb-4 hover:cursor-pointer"
            onClick={()=>handleClick(les)}
          >
            <h1 className="text-md font-bold">{les.title}</h1>
            <div className="text-xl pt-1">{getIcon(les.type)}</div>
          </div>
        );
      })}
    </div>
  );
}
