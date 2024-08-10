import React, { useEffect } from 'react'
import PlaneComp from '../PlaneComp'
import useFetch from '../AuthComponents/UseFetch';

export default function Plane() {

  const { fetchData , resData } = useFetch();

  useEffect(()=>{
      const getPlanes = async () => {
        const res = await fetchData({url: 'http://127.0.0.1:8000/api/planes/', method: 'get'}) 
        console.log(res);
      }
        getPlanes();
  },[])

  return (
    <section class="bg-primary dark:bg-DarkGray rounded py-12">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-extrabold text-white sm:text-5xl">
            Pricing Plans
          </h2>
          <p class="mt-4 text-xl text-gray-400">
            Choose your plans please
          </p>
        </div>
    
        <div class="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-3">
          {resData?.map((item)=>{
            return <PlaneComp key={item?.id} data={item} /> 
          })}
        </div>
      </div>
    </section>
  )
}
