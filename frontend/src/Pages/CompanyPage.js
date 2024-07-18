import React, { useEffect } from 'react'
import Navbar2 from '../Components/Navbar2'
import Company2 from '../Components/Company2'
import logo from '../images/logo.png'
import UseFetch from '../Components/AuthComponents/UseFetch'
import Loader from '../Components/Loader'


export default function CompanyPage() {
  const { fetchData , resData , loading , error } = UseFetch();
  useEffect(()=>{
    const getCompany = async ()=>{
      const res = await fetchData({
        method: "get",
        url: "http://127.0.0.1:8000/api/get_companies/",
        data: {},
        params: {},
        headers:{}
      })
      console.log(res);
    }
    getCompany();
  },[])
  return (
    <>
    <Navbar2 name={resData?.username}/>
    <div className="container mx-auto">
        <h1 className='font-black text-4xl p-8'>Companies:</h1>
        {
          resData ? 
          <div className='grid grid-cols-3 gap-10 px-10'>
                {
                  resData?.companies?.map((company)=>{
                    return <Company2 key={company.id} image={company.logo} id={company.id} name={company.name} />
                    })
                }
        </div>
          : 
          <div className='container w-[100%] h-[100%] flex justify-center items-center sm:px-4'>
            <Loader />
          </div> 
        }
    </div>
    </>
  )
}
