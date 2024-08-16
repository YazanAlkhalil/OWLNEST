import ProgressBar from "@ramonak/react-progress-bar";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaHeart, FaStar } from "react-icons/fa";
import useFetch from "./AuthComponents/UseFetch";

export default function TraineeCourse({ data, id }) {
  const navigate = useNavigate();
  const { fetchData } = useFetch();
  const [fav, setFav] = useState(data?.is_favourite);
  const companyID = localStorage.getItem("companyId");

  console.log("course ID", id);




  const handleIconClick = async () => {
    if (!fav) {

      const data1 = {
        course: id,
      };
      const res = await fetchData({
        url:
          "http://127.0.0.1:8000/api/trainee/company/" + companyID + "/favorites",
        method: "post",
        data: data1,
      });
      setFav(true);
    }
    else {
      const data = {
        course: id
      }
      const res = await fetchData({ url: 'http://127.0.0.1:8000/api/trainee/company/' + companyID + '/favorites', method: 'delete', data: data })
      setFav(false);
      console.log(res);
    }
  };
  return (
    <div onClick={() => {
      navigate(`/trainee/courses/${id}/content`);
    }} className="">
      <img
        className="w-[330px] h-48 hover:cursor-pointer border rounded"
        src={data?.image}
        alt="error"

      />
      <ProgressBar
        completed={data?.progress}
        labelColor="#FFFFFF"
        bgColor="#001f34"
        transitionDuration="2s"
        transitionTimingFunction="linear"
        animateOnRender
        className="mt-3"
      />
      <div className="text-xl dark:bg-DarkGray font-semibold w-[330px] mt-2 py-1 px-2">
        {data?.name}
      </div>
      <div className="px-2 py-1 text-xl flex justify-between">
        <h1 className="font-semibold">By {data?.leader}</h1>
        <FaHeart
          className={`${fav ? "text-red-600" : "text-slate-500"
            } hover:cursor-pointer`}
          onClick={handleIconClick}
        />
      </div>
    </div>
  );
}
