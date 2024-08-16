import React, { useEffect, useState } from "react";
import Instructor from "../Instructor";
import useFetch from "../AuthComponents/UseFetch";
import { useParams } from "react-router-dom";

export default function TraineeInfor() {
  const {fetchData}= useFetch()
  const {id} = useParams()
  const [description,setDescription] = useState("")
  const [trainers,setTrainers] = useState([])
  const [resources,setResources] = useState("")

  useEffect(()=>{
    const getInfo = async ()=>{
      const res =await fetchData({url:'/courses/'+id+'/info'})
      console.log(res);
      setDescription(res.description)
      setResources(res.resource)
      setTrainers(res.trainers)
    }
    getInfo()
  },[])
  return (
    <div>
      <div className="px-8 ">
        <h1 className="text-2xl font-black">Course Instructor</h1>
        {trainers.map((trai) => {
          return <Instructor key={trai.id} name={trai.username} image={trai.image_url}/>;
        })}
      </div>
      <div className="w-[200px] dark:bg-white bg-slate-950 h-[3px] mx-auto my-8 "></div>
      <div className="px-8">
        <h1 className="text-2xl font-black my-8">Description</h1>
        <h1 className="text-xl font-bold w-[90%] mx-auto ">
          {description}
        </h1>
      </div>
      <div className="w-[200px] dark:bg-white bg-slate-950 h-[3px] mx-auto my-10"></div>
      <div className="px-8">
        <h1 className="text-2xl font-black my-8">Additional Resources</h1>
        <h1 className="text-xl font-bold w-[90%] mx-auto ">{resources}</h1>
      </div>
    </div>
  );
}
