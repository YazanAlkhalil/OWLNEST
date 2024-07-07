import React from 'react'
import Card from '../../Components/Card'
import ChartExample from '../../Components/Chart'
import { NavLink } from 'react-router-dom'




function AdminDashboard() {
  return (
    <div className='flex flex-col h-full'>
        <div className='flex justify-between items-center'>
            <span className='text-xl '>Owner: yazan Alkhalil</span>
            <div>
                <span className='text-lg mr-5'>Balance: 2345$</span>
                <NavLink to={'/admin/buyCourse'} className='bg-accent text-white p-2 rounded hover:bg-[#dea01edd]'>Buy Courses</NavLink>
            </div>
        </div>
        <div className='flex justify-evenly flex-grow my-8'>

        {/* <Card title={'Trainees'} value={"234"} />
        <Card title={'Trainers'} value={"134"} />
        <Card title={'Admins'} value={"32"} />
        <Card title={'Total Course Completions'} value={"1002"} /> */}
        <div className='flex text-lg bg-secondary text-white  justify-around w-full py-4 rounded'>
            <div className='flex flex-col items-center'>
                <div>Trainees</div>
                <div>234</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Trainers</div>
                <div>234</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Admins</div>
                <div>234</div>
            </div>
            <div className='flex flex-col items-center'>
                <div>Total Course Completions</div>
                <div>1002</div>
            </div>
            
        </div>
        </div>
        <ChartExample options={{
    height: 380,
    title: {
      text: "Courses Completions",
    },
    data: [
        { month: "Jan", "Courses": 200 },
        { month: "Feb", "Courses": 210 },
        { month: "Mar", "Courses": 195 },
        { month: "Apr", "Courses": 205 },
        { month: "May", "Courses": 215 },
        { month: "Jun", "Courses": 200 },
        { month: "Jul", "Courses": 225 },
        { month: "Aug", "Courses": 210 },
        { month: "Sep", "Courses": 250 },
        { month: "Oct", "Courses": 205 },
        { month: "Nov", "Courses": 215 },
        { month: "Dec", "Courses": 220 },
      ],
    series: [
      {
        type: "area",
        xKey: "month",
        yKey: "Courses",
        yName: "Courses",
      },
      
    ],
  }}/>
        
    </div>
  )
}

export default AdminDashboard
