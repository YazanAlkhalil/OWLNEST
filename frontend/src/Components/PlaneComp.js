import React from "react";
import useFetch from "./AuthComponents/UseFetch";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

export default function PlaneComp({ data }) {
  const { fetchData, resData } = useFetch();
  const navigate = useNavigate();

  const handleBuyButtonClick = async () => {
    const id = {
        "plane_id" : data?.id
    }
    const res = await fetchData({
      url: "http://127.0.0.1:8000/api/buyPlane/",
      method: "post",
      data: id
    }).then((data)=>{
        navigate('/admin/dashboard',{replace: true});
        toast.success('Mission Complete')
    }).catch((err)=>{
        console.log(err);
        toast.error(err);
    });
    console.log(res);
  };

  return (
    <div>
      <div class="bg-gray-800 rounded-lg shadow-lg p-6 transform hover:scale-105 transition duration-300">
        <div class="mb-8">
          <h3 class="text-2xl font-semibold text-white">{data?.plane_name} </h3>
          <p class="mt-4 text-gray-400">Get started with our features.</p>
        </div>
        <div class="mb-8">
          <span class="text-xl font-extrabold text-white">{data?.price} </span>
          <span class="text-md font-medium text-gray-400">SP</span>
        </div>
        <ul class="mb-8 space-y-4 text-gray-400">
          <li class="flex items-center">
            <svg
              class="h-6 w-6 text-green-500 mr-2"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
            <span>{data?.subscription_term} </span>
          </li>
          <li class="flex items-center">
            <svg
              class="h-6 w-6 text-green-500 mr-2"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor">
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              />
            </svg>
            <span>{data?.courses_number} Courses</span>
          </li>
        </ul>
        <button
          onClick={handleBuyButtonClick}
          class="block w-full py-3 px-6 text-center rounded-md text-white font-medium bg-secondary">
          Buy Now
        </button>
      </div>
    </div>
  );
}
