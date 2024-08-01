import React, { useEffect, useState } from 'react'
import TrainerCourse from '../../Components/TrainerCourse'
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import image3 from '../../images/c_7_free_google_courses_become_machine_learning_engineer_1 1.png'
import image4 from '../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import FormDialog from '../../Components/admin/AddCourseDialog'
import useFetch from '../../Components/AuthComponents/UseFetch'



function AdminCoursesPage() {
    const [courses,setCourses]= useState([])
    const companyId = localStorage.getItem('companyId')
    const {fetchData} = useFetch()
    async function getCourses(){
        const res = await fetchData({url: 'http://127.0.0.1:8000/api/admin/company/'+companyId+'/courses'});
        if (Array.isArray(res)) {
            setCourses(res)
            
        }
    }
    useEffect(()=>{
        getCourses()  
    },[])
    return (
        <div className='flex flex-col'>
        <FormDialog getCourses={getCourses}/>
        <div className='grid grid-cols-3 gap-y-10'>
            {courses.map(course => (
                <TrainerCourse key={course.id} id={course.id} image={course.image} name={course.name}/>
            ))}
        </div>
        </div>
    )
}

export default AdminCoursesPage
