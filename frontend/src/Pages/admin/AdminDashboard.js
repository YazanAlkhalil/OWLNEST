import React, { useEffect, useState } from 'react'
import Card from '../../Components/Card'
import ChartExample from '../../Components/Chart'
import { NavLink } from 'react-router-dom'
import { useSelector } from 'react-redux';
import useFetch from '../../Components/AuthComponents/UseFetch';




function AdminDashboard() {
  const isOwner = localStorage.getItem('isOwner')
  const isDarkMode = useSelector((state) => state.theme.isDarkMode);
  const [owner,setOwner] = useState("")
  const [trainers,setTrainers] = useState("")
  const [trainees,setTrainees] = useState("")
  const [completions,setCompletions] = useState([])
  const [admins,setAdmins] = useState("")
  const [totalCompletions,setTotalCompletions] = useState("")
  const companyId = localStorage.getItem('companyId');
  const {fetchData} = useFetch()

  useEffect(()=>{
    const getData = async ()=>{

      const res = await fetchData({url:"/admin/company/"+companyId+"/dashboard"})
      console.log(res);
      setOwner(res.owner)
      setTrainees(res.trainees)
      setTrainers(res.trainers)
      setAdmins(res.admins)
      setTotalCompletions(res.total_completions)
      setCompletions(res.graph)
    }
    getData()
  },[])


  return (
    <div className='flex flex-col h-full'>
        <div className='flex justify-between items-center'>
            <span className='text-xl '>Owner: {owner}</span>
            {isOwner === 'true' && <div>
                <span className='text-lg mr-5'>Balance: 2345$</span>
                <NavLink to={'/admin/buyCourse'} className='bg-accent text-white p-2 rounded hover:bg-[#dea01edd]'>Buy Courses</NavLink>
            </div>}
        </div>
        <div className='flex justify-evenly flex-grow my-8'>

        {/* <Card title={'Trainees'} value={"234"} />
        <Card title={'Trainers'} value={"134"} />
        <Card title={'Admins'} value={"32"} />
        <Card title={'Total Course Completions'} value={"1002"} /> */}
        <div className='flex text-lg bg-secondary dark:bg-DarkSecondary text-white  justify-around w-full py-4 rounded'>
            <div className='flex flex-col items-center'>
                <div>Trainees</div>
                <div>{trainees}</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Trainers</div>
                <div>{trainers}</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Admins</div>
                <div>{admins}</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Total Course Completions</div>
                <div>{totalCompletions}</div>
            </div>
            
        </div>
        </div>
        <ChartExample options={{
    height: 380,
    theme: !isDarkMode ? 'ag-default-dark' : 'ag-default',
    title: {
      text: "Courses Completions",
    },
    data: completions,
    series: [
      {
        type: "area",
        xKey: "month",
        yKey: "completions",
        yName: "completions",
      },
      
    ],
  }}/>
        
    </div>
  )
}

export default AdminDashboard
