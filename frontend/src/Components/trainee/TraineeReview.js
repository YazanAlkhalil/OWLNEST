import React, { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import useFetch from '../AuthComponents/UseFetch';

export default function TraineeReview() {
    const {id} = useParams();
    const companyId = localStorage.getItem('companyId');
    const { fetchData , resData } = useFetch();
    useEffect(()=>{
       const getReviews = async () =>{
        const res = await fetchData({url: `http://127.0.0.1:8000/api/trainee/company/${companyId}/courses/${id}/review`, method: 'get'}) 
        console.log(res);
        
       }
       getReviews();
    },[])
  return (
    <div className="p-6 min-h-screen">
            {resData?.map((item) => (
                <div key={item.id} className=" shadow-md rounded-lg p-6 mb-6">
                    <h2 className="text-xl font-bold mb-4">{item.course.name}</h2>
                    <img src={item.course.image} alt={item.course.name} className="w-32 h-auto rounded mb-4" />
                    <p className="text-gray-500 mb-2">Review: {item.description}</p>
                    <p className="text-gray-500 mb-2">By: mootaz Trainee</p>
                    <p className="text-gray-500">Rate: {item.rate}</p>
                </div>
            ))}
        </div>
  )
}
