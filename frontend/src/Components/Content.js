import React from "react";
import { FaPlay, FaRegFilePdf } from "react-icons/fa";
import { PiExam } from "react-icons/pi";
import { useNavigate } from "react-router-dom";

function getIcon(icon) {
  if (icon === "video") return <FaPlay />;
  else if (icon === "pdf") return <FaRegFilePdf />;
  else return <PiExam />;
}

export default function Content({ unit, lessons }) {
    const navigate = useNavigate();
  return (
    <div className="m-3">
      <h1 className="mb-4 font-semibold text-xl">{unit} :</h1>
      {lessons.map((les) => {
        return (
          <div
            key={les.id}
            className="flex justify-between bg-gray-300 px-6 py-3 mb-4 hover:cursor-pointer"
            onClick={()=> navigate('/trainee/courses/:id/content/lesson')}
            >
            <h1 className="text-md font-bold">{les.title}</h1>
            <div className="text-xl pt-1">{getIcon(les.type)}</div>
          </div>
        );
      })}
    </div>
  );
}
