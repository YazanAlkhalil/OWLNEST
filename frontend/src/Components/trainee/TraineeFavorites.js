import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import photo from './../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png';
import photo1 from './../../images/multimedia-courses-scope-and-career 1.png';
import ProgressBar from "@ramonak/react-progress-bar";
import { FaStar } from "react-icons/fa";

const favourits = [
  {
    id: 1,
    image: photo,
    title: "Data Structures from C to Python",
    trainer : 'Mootaz alhalak'
  },
  {
    id: 2,
    image: photo,
    title: "Data Structures from C to Python",
    trainer : 'Yazona'
  },
  {
    id: 3,
    image: photo1,
    title: "Multimedia",
    trainer : 'Ahmed mohamed'
  },
  {
    id: 4,
    image: photo1,
    title: "Multimedia",
    trainer : 'Ahmed mohamed'
  },
  {
    id: 5,
    image: photo1,
    title: "Multimedia",
    trainer : 'Ahmed mohamed'
  },
];

export default function TraineeFavorites() {
  const navigate = useNavigate();
  const [fav,setFav] = useState(false);

  function handleIconClick(){
    setFav(true);
    console.log('hi')
  }
  return (
    <div className="flex flex-wrap gap-3">
      {favourits.map((fav)=>{
        return (
          <div
        className="hover:cursor-pointer"
        key={fav.id}>
        <img className="w-[330px] border  rounded" src={fav.image}  onClick={() => {navigate("/trainee/courses/id");}} />
        <ProgressBar
        completed={50}
        labelColor="#FFFFFF"
        bgColor="#001f34"
        transitionDuration="2s"
        transitionTimingFunction="linear"
        animateOnRender
        className="border-none outline-none mt-3"
      />
        <div className="text-xl font-semibold w-[330px] mt-2 py-1 px-2">
          {fav.title}
        </div>
        <div className="px-2 py-1 text-xl flex justify-between"> 
        <h1 className="font-semibold">By {fav.trainer}</h1>
        <FaStar className="text-accent" onClick={handleIconClick} />
        </div>

      </div>
        )
      })}
    </div>
  );
}
