import React, { useEffect, useState } from 'react'
import TrainerCourse from '../../Components/TrainerCourse'
import image from '../../images/multimedia-courses-scope-and-career 1.png'
import image2 from '../../images/BA-Courses 1.png'
import image3 from '../../images/c_7_free_google_courses_become_machine_learning_engineer_1 1.png'
import image4 from '../../images/course__cs101_courses_datastructuresfromctopython__course-promo-image-1653540139 1.png'
import FormDialog from '../../Components/admin/AddCourseDialog'
import useFetch from '../../Components/AuthComponents/UseFetch'



function AdminCoursesPage({ pending }) {
    const [courses, setCourses] = useState([])
    const companyId = localStorage.getItem('companyId')
    const { fetchData } = useFetch()
    async function getCourses() {
        const res = await fetchData({ url: 'http://127.0.0.1:8000/api/admin/company/' + companyId + '/courses' });
        if (Array.isArray(res)) {
            setCourses(res)

        }
    }
    async function getPendingCourses() {
        const res = await fetchData({ url: 'http://127.0.0.1:8000/api/admin/company/' + companyId + '/pending_courses' });
        if (Array.isArray(res)) {
            setCourses(res)

        }
    }
    useEffect(() => {
        if (!pending)
            getCourses()
        else
            getPendingCourses()
    }, [])
    return (
        <div className='flex flex-col'>

            {!pending && <FormDialog getCourses={getCourses} />}
            {
                courses.length > 1 ?
                    <div className='grid grid-cols-3 gap-y-10'>
                        {courses.map(course => (
                            <TrainerCourse key={course.id} id={course.id} image={course.image} name={course.name} />
                        ))}
                    </div>
                    : (
                        <div className="flex w-full flex-col items-center ">
                            <div className=" shadow-md rounded-lg p-8 max-w-md w-full">
                                <div className="flex flex-col items-center">
                                    <svg
                                        className="h-16 w-16  mb-4"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                    >
                                        <path
                                            strokeLinecap="round"
                                            strokeLinejoin="round"
                                            strokeWidth={2}
                                            d="M9 13h6m-3-3v6m-9 1V7a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z"
                                        />
                                    </svg>
                                    <h2 className="text-2xl font-bold  mb-2">
                                        No Courses Available
                                    </h2>
                                    <p className="mb-6">
                                        It looks like there are no courses at the moment.
                                    </p>
                                </div>
                            </div>
                        </div>
                    )}
        </div>
    )
}

export default AdminCoursesPage
