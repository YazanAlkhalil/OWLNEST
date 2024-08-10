import React, { useEffect, useState } from 'react'
import BasicTable from './Table'
import image from '../images/simple-user-default-icon-free-png.webp'
import useFetch from './AuthComponents/UseFetch'
import { useParams } from 'react-router-dom'
function CourseTrainees() {
  const {fetchData } = useFetch()
  const [data,setData] = useState([])
  const {id} = useParams()
  useEffect(()=>{
    const getUsers = async ()=>{
      const res = await fetchData({url:"http://127.0.0.1:8000/api/trainer/course/"+id+"/users"})
      setData(res)
    }
    getUsers()
  },[])


  return (
    <div className='text-2xl'>
      <BasicTable heading={['Name','Progress','XP','Grades','Completed']} 
      data={data}
      />
    </div>
  )
}

export default CourseTrainees
