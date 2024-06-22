import React from 'react'
import ChartExample from './Chart'
import Card from './Card'

function CourseReports({admin}) {
  return (
    <div className='flex flex-col'>

      {admin && <h1 className='text-xl '>Admin : yazona</h1>}
      <div className='flex justify-between'>
        <Card title={'learner in progress'} value={'246'}/>
        <Card title={'completed learners'} value={'234'}/>
        <Card title={'Average grades'} value={'76%'}/>
        <Card title={'Instructors'} value={'2'}/>
        
      </div>
      <div className='mt-auto'>

        <ChartExample options={{
    height: 380,
    title: {
      text: "XP gains for trainees",
    },
    data: [
        { month: "Jan", "XP gains": 200 },
        { month: "Feb", "XP gains": 210 },
        { month: "Mar", "XP gains": 195 },
        { month: "Apr", "XP gains": 205 },
        { month: "May", "XP gains": 215 },
        { month: "Jun", "XP gains": 200 },
        { month: "Jul", "XP gains": 225 },
        { month: "Aug", "XP gains": 210 },
        { month: "Sep", "XP gains": 250 },
        { month: "Oct", "XP gains": 205 },
        { month: "Nov", "XP gains": 215 },
        { month: "Dec", "XP gains": 220 },
      ],
    series: [
      {
        type: "area",
        xKey: "month",
        yKey: "XP gains",
        yName: "XP gains",
      },
      
    ],
  }}/>
      </div>
    </div>
  )
}

export default CourseReports
