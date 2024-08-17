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
    <div className="m-6 rounded-lg shadow-md p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className={`font-bold text-2xl`}>{data.title}</h1>
        {data?.is_completed ? (
          <span className="bg-green-500  px-3 py-1 rounded-full text-sm font-semibold">
            Completed
          </span>
        ) : (
          <span className="bg-yellow-500  px-3 py-1 rounded-full text-sm font-semibold">
            In Progress
          </span>
        )}
      </div>
      <div className="space-y-3">
        {data.contents.map((les) => {
          return (
            <div
              key={les.id}
              className={`flex justify-between items-center p-4 rounded-lg transition-all duration-300 ease-in-out ${
                les.is_completed
                  ? 'bg-green-100 hover:bg-green-200'
                  : 'bg-gray-100 dark:bg-DarkSecondary dark:hover:bg-DarkGrayHover hover:bg-gray-200'
              } cursor-pointer`}
              onClick={() => handleClick(les)}
            >
              <div className="flex items-center space-x-3">
                <div className={`text-2xl ${les.is_completed ? 'text-green-500' : 'dark:text-white text-gray-500'}`}>
                  {getIcon(les.type)}
                </div>
                <h1 className={`text-lg font-semibold ${les.is_completed ? 'text-green-700' : ' dark:text-white text-gray-700'}`}>
                  {les.title}
                </h1>
              </div>
              {les.is_completed && (
                <svg className="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M5 13l4 4L19 7"></path>
                </svg>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}