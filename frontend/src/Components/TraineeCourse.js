import ProgressBar from "@ramonak/react-progress-bar";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaStar } from "react-icons/fa";
import useFetch from "./AuthComponents/UseFetch";

export default function TraineeCourse({ data }) {
  const navigate = useNavigate();
  const { fetchData } = useFetch();
  const [fav, setFav] = useState(false);
  const companyID = localStorage.getItem("companyId");

  console.log("course ID",data?.id);

  const handleIconClick = async () => {
    const data1 = {
      course: data?.id,
    };
    setFav(true);
    const res = await fetchData({
      url:
        "http://127.0.0.1:8000/api/trainee/company/" + companyID + "/favorites",
      method: "post",
      data: data1,
    });
  };
  return (
    <div className="">
      <img
        className="w-[330px] hover:cursor-pointer border rounded"
        src={data?.image}
        alt="error"
        onClick={() => {
          navigate(`/trainee/courses/${data?.id}/content`);
        }}
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
        <FaStar
          className={`${
            data?.is_favourite || fav ? "text-accent" : "text-slate-500"
          } hover:cursor-pointer`}
          onClick={handleIconClick}
        />
      </div>
    </div>
  );
}
